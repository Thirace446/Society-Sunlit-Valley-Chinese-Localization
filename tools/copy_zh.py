import shutil
import logging
from pathlib import Path

def setup_logging():
    """配置日志系统，同时输出到控制台和 log.txt 文件"""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # 文件处理器 (输出到 log.txt)
    file_handler = logging.FileHandler("log.txt", encoding='utf-8')
    file_handler.setFormatter(formatter)

    # 控制台处理器 (显示在屏幕上)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def mirror_zh_cn_with_log():
    # 初始化日志
    setup_logging()
    
    # 1. 设置路径
    base_dir = Path(__file__).parent.absolute()
    src_root = base_dir / "assets"
    dst_root = base_dir / "copy"

    if not src_root.exists():
        logging.error(f"未找到源目录: {src_root}")
        return

    logging.info(f"开始任务: 从 {src_root} 镜像 zh_cn.json 到 {dst_root}")
    
    count = 0
    
    # 2. 遍历查找
    # 查找所有子目录下的 zh_cn.json
    for src_file in src_root.rglob("zh_cn.json"):
        try:
            # 3. 计算相对路径
            relative_path = src_file.relative_to(src_root)
            dst_file = dst_root / relative_path

            # 4. 创建目标目录
            dst_file.parent.mkdir(parents=True, exist_ok=True)

            # 5. 复制文件
            shutil.copy2(src_file, dst_file)
            
            logging.info(f"[成功] 复制: {relative_path}")
            count += 1
            
        except Exception as e:
            logging.error(f"[失败] 处理 {src_file.name} 时出错: {str(e)}")

    # 6. 结束总结
    logging.info(f"任务结束。共复制文件: {count} 个。")
    logging.info("-" * 50) # 在日志中划个分界线

if __name__ == "__main__":
    mirror_zh_cn_with_log()