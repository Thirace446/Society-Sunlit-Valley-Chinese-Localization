import os
import json
from pathlib import Path
import datetime

# --- 配置区 ---
VALLEY_DIR = "valley"
COBBLE_DIR = "cobblemon"
LOG_FILE = "log.md"
REPORT_FILE = "report.json"

def write_log(message, mode="a"):
    """记录日志到文件和控制台"""
    with open(LOG_FILE, mode, encoding="utf-8") as f:
        f.write(message + "\n")

def load_json(path):
    """安全加载JSON，文件不存在或解析失败返回None"""
    if not path.exists():
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except:
        return {}

def compare_en_us_keys(dict_v, dict_c):
    """
    对比两个已存在的JSON内容。
    返回：(详细对比报告字典, 是否有差异, 差异键名列表)
    """
    all_keys = sorted(set(dict_v.keys()) | set(dict_c.keys()))
    full_report = {}
    diff_keys = []

    for key in all_keys:
        val_v = dict_v.get(key)
        val_c = dict_c.get(key)

        if key in dict_v and key in dict_c:
            if val_v == val_c:
                status = "完全一致"
            else:
                status = "值冲突"
                diff_keys.append(key)
        elif key in dict_v:
            status = "Valley独有键"
            diff_keys.append(key)
        else:
            status = "Cobblemon独有键"
            diff_keys.append(key)

        full_report[key] = {
            "status": status,
            "valley_value": val_v,
            "cobblemon_value": val_c
        }
        
    return full_report, len(diff_keys) > 0, diff_keys

def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_log(f"=== 模组对比报告 ({timestamp}) ===\n", mode="w")

    p_valley = Path(VALLEY_DIR)
    p_cobble = Path(COBBLE_DIR)

    if not p_valley.exists() or not p_cobble.exists():
        print(f"错误：找不到 {VALLEY_DIR} 或 {COBBLE_DIR} 文件夹。")
        return

    # 获取文件夹集合
    mods_v = {d.name for d in p_valley.iterdir() if d.is_dir()}
    mods_c = {d.name for d in p_cobble.iterdir() if d.is_dir()}

    # 1. 识别文件夹缺失情况
    only_in_valley = sorted(list(mods_v - mods_c))
    only_in_cobble = sorted(list(mods_c - mods_v))
    common_mods = sorted(list(mods_v & mods_c))

    # --- 执行内容对比 (仅针对共有文件夹) ---
    report_data = {}
    mods_with_diffs = [] 
    identical_mods_count = 0

    print(f"正在分析 {VALLEY_DIR} 和 {COBBLE_DIR} 的共有模组...")

    for mod in common_mods:
        file_v = p_valley / mod / "lang" / "en_us.json"
        file_c = p_cobble / mod / "lang" / "en_us.json"

        data_v = load_json(file_v)
        data_c = load_json(file_c)

        # 逻辑：只要双方至少有一个 en_us.json 存在，就尝试对比
        if data_v is not None and data_c is not None:
            report, has_diff, diff_keys = compare_en_us_keys(data_v, data_c)
            report_data[mod] = report
            
            if has_diff:
                mods_with_diffs.append({"name": mod, "keys": diff_keys})
            else:
                identical_mods_count += 1
        else:
            # 如果文件夹在，但 lang/en_us.json 文件缺失
            missing_msg = []
            if data_v is None: missing_msg.append(f"{VALLEY_DIR}侧缺失en_us.json")
            if data_c is None: missing_msg.append(f"{COBBLE_DIR}侧缺失en_us.json")
            mods_with_diffs.append({"name": mod, "keys": [f"文件错误: {' & '.join(missing_msg)}"]})

    # --- 写入 log.md ---
    # 第一部分：仅列出缺失的文件夹名
    write_log("【1. 缺失的模组文件夹 / Missing Folders】")
    if only_in_valley:
        write_log(f"▶ 仅在 {VALLEY_DIR} 中存在的文件夹 (Cobblemon中缺失):")
        for m in only_in_valley: write_log(f"   - {m}")
    
    if only_in_cobble:
        write_log(f"\n▶ 仅在 {COBBLE_DIR} 中存在的文件夹 (Valley中缺失):")
        for m in only_in_cobble: write_log(f"   - {m}")
        
    if not only_in_valley and not only_in_cobble:
        write_log("   (两侧文件夹列表完全一致)")

    # 第二部分：共有文件夹中的键名差异
    write_log("\n【2. 共有模组的内容差异 / Content Differences】")
    if mods_with_diffs:
        for item in mods_with_diffs:
            write_log(f"▶ 模组名: {item['name']}")
            for k in item['keys']:
                write_log(f"   - {k}")
            write_log("-" * 45)
    else:
        write_log("   (所有共有模组的翻译内容均完全相同)")

    write_log(f"\n【3. 统计汇总】")
    write_log(f"   - 共有模组总数: {len(common_mods)}")
    write_log(f"   - 完全一致的模组: {identical_mods_count}")
    write_log(f"   - 存在内容差异的模组: {len(mods_with_diffs)}")

    # --- 写入 report.json ---
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

    print(f"分析完成！")
    print(f"- 差异摘要和缺失文件夹请看: {LOG_FILE}")
    print(f"- 详细翻译值对比请看: {REPORT_FILE}")

if __name__ == "__main__":
    main()