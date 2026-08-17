# 阳光谷 NPC 好感度总览

- 来源: `kubejs/startup_scripts/globalNPCHandlers.js` (`villagerSpecificGifts` + UNIVERSAL 列表),通过 `global.getVillagerGiftResult()` 判定。
- 其他来源: https://sunlitvalley.miraheze.org/wiki/Villagers
- 数据版本：4.1.3 
- 整理：Thirace
- 阳光谷汉化官方反馈群：700510144

## 好感度变化

- 常规 NPC 每天第一次交谈 +5 好感度
- 智慧橡树 每天第一次交谈 +20 好感度

| 礼物类型 | 好感度变化 |
| --- | --- |
| loved (最爱) | +40 |
| liked (喜欢) | +25 |
| neutral (一般) | +10 |
| disliked (讨厌) | -15 |
| hated (厌恶) | -30 |

- 送礼有 **3 天冷却**。
 - 例 1: 送苔藓莓给玛丽亚 → 苔藓莓是她最爱的礼物 +40 好感度，但送给其他人只是喜欢所以 +25 好感度。
 - 例 2: 送兔子脚给玛丽亚 → 兔子脚虽是人见人爱的礼物,但玛丽亚很讨厌它,就会 -30 好感度。

## 好感度奖励里程碑

好感累积达到 500 后(一次性)触发「满好感奖励」;持有对应技能书阶段时部分奖励会变化。满好感且达到 `trainer_lvl_8` 阶段后还有一次「神秘礼物」。**除满好感外无其他奖励档位**(中间 100~400 档只改变对话内容)。

### 满好感奖励 (好感 = 500)

| NPC | 奖励 | 其他奖励 |
| --- | --- | --- |
| banker (凯若琳 · 银行家) | 向艺术跋涉 (技能书) | 如已学会此技能,改为赠送 2× 传送石碑 `waystones:waystone` |
| market (里昂 · 市场商人) | 通用耕作方法 (技能书) | 如已学会此技能,改为赠送 16× 火花豆种子 `society:sparkpod_seed` |
| librarian (维罗妮卡 · 图书管理员) | 债务洞穴 (技能书) | 如已学会此技能,改为赠送 女王之魅 `botania:diva_charm` + 魔力之戒 `botania:mana_ring` |
| trader (卡洛斯 · 交易商) | 解锁服装店 |
| blacksmith (艾登 · 铁匠) | 艾登之锤 `justhammers:iron_hammer` 效率 V 时运 III |
| carpenter (艾斯 · 木匠) | 破旧蓝图:Blockapedia `portable_blueprints:worn_blueprint` |
| fisher (春奈 · 渔夫) | 海王之心 `society:heart_of_neptunium` |
| shepherd (玛利亚 · 牧羊人) | 2× 企鹅刷怪蛋 `wildernature:penguin_spawn_egg` |
| witch (伊芙琳 · 女巫) | 自动抚摸器 `society:auto_petter` |
| wise_oak (智慧橡树) | 解锁智慧橡树商店 |

### Sunlit Cobblemon 神秘礼物 (好感500 + 训练家等级达到：大师级)

给予对应宝可梦的 `sunlit_cobblemon:mystery_gift` 

| NPC | 宝可梦 |
| --- | --- |
| banker (凯若琳 · 银行家) | 玛夏多 (Marshadow) |
| blacksmith (艾登 · 铁匠) | 玛机雅娜 (Magearna) |
| carpenter (艾斯 · 木匠) | 雪拉比 (Celebi) |
| fisher (春奈 · 渔夫) | 波尔凯尼恩 (Volcanion) |
| market (里昂 · 市场商人) | 捷拉奥拉 (Zeraora) |
| shepherd (玛利亚 · 牧羊人) | 美洛耶塔 (Meloetta) |

librarian、trader、witch、wise_oak 无神秘礼物。

## 通用列表 (对所有 NPC 生效)

### 最爱 (UNIVERSAL_LOVED) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 五彩碎片 | `society:prismatic_shard` |
| 兔子脚 | `minecraft:rabbit_foot` |
| 乌龙茶 | `herbalbrews:oolong_tea` |
| 阳光珍珠 | `society:sunlit_pearl` |
| Jellie猫咪葡萄酒 | `vinery:jellie_wine` |
| 侏儒 | `society:gnome` |
| 灵魂茶 | `society:bowl_of_soul` |
| 珍珠块 | `crabbersdelight:pearl_block` |

### 喜欢 (UNIVERSAL_LIKED) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意毛衣 | `#etcetera:sweaters` |
| 任意帽子 | `#etcetera:hats` |
| 任意矿产 | `#society:mineral` |
| 任意宝石 | `#forge:gems` |
| 任意无瑕矿产 | `#society:pristine_mineral` |
| 不死图腾 | `minecraft:totem_of_undying` |
| 糖渍橙子片 | `atmospheric:candied_orange_slices` |
| 钻石之心 | `quark:diamond_heart` |
| 苔藓莓 | `society:mossberry` |
| 苔藓莓沙拉 | `society:mossberry_stew` |
| 珍珠 | `crabbersdelight:pearl` |
| 家具盒 | `society:furniture_box` |
| 古代饼干 | `society:ancient_cookie` |

### 讨厌 (UNIVERSAL_DISLIKED) -15 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意原木 | `#society:raw_logs` |
| 经验块 / 经验颗粒 | `create:experience_block` / `create:experience_nugget` |
| 霜冻火腿 / 霜冻猪排 | `snowpig:frozen_ham` / `snowpig:frozen_porkchop` |
| 油 | `society:oil` |
| 竹叶茅草 | `twigs:bamboo_thatch` |
| 冲刺板 | `automobility:dash_panel` |
| 骷髅鱼 / 凋灵骷髅鱼 | `netherdepthsupgrade:bonefish` / `netherdepthsupgrade:wither_bonefish` |
| 熔岩晶球 / 全能晶球 / 冰冻晶球 / 晶球 | `society:magma_geode` / `society:omni_geode` / `society:frozen_geode` / `society:geode` |
| 电池 | `society:battery` |
| 橡树树脂 / 松焦油 | `society:oak_resin` / `society:pine_tar` |
| 棕榈原木 | `beachparty:palm_log` |
| 胭脂外壳 | `atmospheric:carmine_husk` |
| 鹅掌 | `untitledduckmod:goose_foot` |
| 盒子 | `aquaculture:box` |
| 炭化鬼椒 | `vintagedelight:ghost_charcoal` |
| 不祥试炼钥匙 / 试炼钥匙 | `trials:trial_key_ominous` / `trials:trial_key` |
| 下届火龙果沙拉 | `farmersdelight:nether_salad` |
| 皮蛋 | `vintagedelight:century_egg` |
| 海带汁 | `crabbersdelight:kelp_shake` |
| 坚固竹块 | `society:sturdy_bamboo_block` |

### 厌恶 (UNIVERSAL_HATED) -30 好感度

| 物品 | 注册名 |
| --- | --- |
| 海泡菜罐头 | `crabbersdelight:jar_of_pickles` |
| 冬青莓 | `windswept:holly_berries` |
| 海泡菜汁 | `crabbersdelight:sea_pickle_juice` |
| 熔岩河豚 / 眼球鱼 | `netherdepthsupgrade:lava_pufferfish` / `netherdepthsupgrade:eyeball_fish` |
| 河豚 | `minecraft:pufferfish` |
| 秽莓 | `autumnity:foul_berries` |
| 蛋黄酱系列(如 至尊蛋黄酱) | `society:*_mayonnaise` (如 `society:supreme_mayonnaise`) |
| 诡异菌 / 绯红菌 | `minecraft:warped_fungus` / `minecraft:crimson_fungus` |
| 椰子油 | `society:coconut_oil` |
| 烂番茄 | `farmersdelight:rotten_tomato` |
| 毒马铃薯 | `minecraft:poisonous_potato` |
| 锡罐 | `aquaculture:tin_can` |
| 烟草叶干 / 土烟叶 | `society:dried_tubabacco_leaf` / `society:tubabacco_leaf` |
| 下界之星 | `minecraft:nether_star` |
| 草秆 | `farmersdelight:straw` |
| 不祥之瓶 | `trials:ominous_bottle` |
| 回响碎片 | `minecraft:echo_shard` |
| 活体肉 | `society:living_flesh` |
| 爆裂紫颂果 | `minecraft:popped_chorus_fruit` |
| 龙首 / 龙蛋 | `minecraft:dragon_head` / `minecraft:dragon_egg` |
| 腐烂的樱桃 | `vinery:rotten_cherry` |
| 龙鳞 | `quark:dragon_scale` |
| 迷你鬼眼 | `society:mini_oni_eye` |
| 橡胶 / 树脂 | `society:rubber` / `society:sap` |

## NPC 专属礼物

### shepherd (玛利亚 · 牧羊人)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 苔藓莓 | `society:mossberry` |
| 蜘蛛丝 | `society:spider_silk` |
| 摩卡 | `society:mocha` |
| 脏柴茶 | `society:dirty_chai` |
| 美利奴羊毛 | `society:merino_wool` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 肉桂咖啡 | `herbalbrews:cinnamon_coffee` |
| 蔓越莓 | `society:cranberry` |
| 博伊森莓 | `society:boysenberry` |
| 水晶莓 | `society:crystalberry` |
| 鲑鱼莓 | `society:salmonberry` |

#### 讨厌 (disliked) -15 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意矿产 | `#society:mineral` |

#### 厌恶 (hated) -30 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意花 | `#minecraft:flowers` |
| 任意生肉 | `#forge:raw_meat` |
| 兔子脚 | `minecraft:rabbit_foot` |
| 任意鱼 | `#minecraft:fishes` |

### banker (凯若琳 · 银行家)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 传奇墨水 | `society:legendary_ink` |
| 野牛角 | `wildernature:bison_horn` |
| 公爵最爱的菜品 | `candlelight:beef_wellington` |
| 风味山羊奶酪轮 | `society:aged_goat_cheese_block` |
| 山羊奶酪轮 | `meadow:goat_cheese_block` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 松露油 | `society:truffle_oil` |
| 山羊奶酪切片 | `meadow:piece_of_goat_cheese` |
| 神秘糖浆 | `society:mystic_syrup` |
| 炖山羊肉 | `windswept:goat_stew` |
| 上古夜曲 | `society:ancient_vespertine` |

#### 一般 (neutral) +10 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意菜肴 | `#society:dish` |

#### 讨厌 (disliked) -15 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意农产品 | `#society:farmer_product` |

#### 厌恶 (hated) -30 好感度

| 物品 | 注册名 |
| --- | --- |
| 能量滋补水 | `society:energy_drink` |
| 糖果 | `supplementaries:candy` |

### blacksmith (艾登 · 铁匠)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 余烬水晶簇 | `society:ember_crystal_cluster` |
| 蜻蜓翅膀 | `crittersandcompanions:dragonfly_wing` |
| 薰衣草 | `windswept:lavender` |
| 榛子咖啡 | `herbalbrews:hazelnut_coffee` |
| 榛多益 | `bakery:hazelnut_ella` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意花 | `#minecraft:flowers` |
| 任意原材料 | `#forge:raw_materials` |
| 榛子 | `pamhc2trees:hazelnutitem` |
| 烤榛子 | `pamhc2trees:roastedhazelnutitem` |

#### 一般 / 讨厌 / 厌恶: 无

### carpenter (艾斯 · 木匠)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意游戏光盘 | `#gamediscs:game_discs` |
| 蒸汽装置 | `society:steamy_gadget` |
| 苔藓莓沙拉 | `society:mossberry_stew` |
| 沉重核心 | `trials:heavy_core` |
| 豪华士力架 | `vintagedelight:deluxe_granola_bar` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 士力架 | `vintagedelight:chocolate_nut_granola_bar` |
| 果味士力架 | `vintagedelight:fruity_granola_bar` |
| 干草帽 | `vinery:straw_hat` |
| 苔藓莓 | `society:mossberry` |
| 蜜渍苹果 | `create:honeyed_apple` |

#### 一般 (neutral) +10 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意原木 | `#society:raw_logs` |

#### 讨厌 / 厌恶: 无

### fisher (春奈 · 渔夫)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 熟气旋鲳鱼串 | `unusualfishmod:cooked_aero_mono_stick` |
| 公主发刷 | `society:princess_hairbrush` |
| 皮蛋 | `vintagedelight:century_egg` |
| 水魔粉尘 | `society:aquamagical_dust` |
| 海王之心 | `society:heart_of_neptunium` |
| 海洋之心 | `minecraft:heart_of_the_sea` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意鱼 | `#minecraft:fishes` |
| 鹦鹉螺壳 | `minecraft:nautilus_shell` |
| 回响碎片 | `minecraft:echo_shard` |
| 化石蛤蜊 | `crittersandcompanions:clam` |
| 黑莲花 | `botania:black_lotus` |
| 任意饰纹陶罐碎片 | `#minecraft:decorated_pot_sherds` |

#### 一般: 无

#### 讨厌 (disliked) -15 好感度

| 物品 | 注册名 |
| --- | --- |
| 珍珠块 | `crabbersdelight:pearl_block` |

#### 厌恶: 无

### market (里昂 · 市场商人)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意红酒 | `#vinery:red_wine` |
| 故障 VHS | `society:glitched_vhs` |
| 远古羽毛 | `windswept:elder_feather` |
| 拿铁 | `society:latte` |
| 土烟烟盒 | `society:tubasmoke_carton` |
| 上古夜曲 | `society:ancient_vespertine` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 土烟 | `society:tubasmoke_stick` |
| 能量滋补水 | `society:energy_drink` |
| 古式墨水 | `supplementaries:antique_ink` |
| 咖啡 | `herbalbrews:coffee` |
| 鸭毛 | `untitledduckmod:duck_feather` |

#### 一般 / 讨厌: 无

#### 厌恶 (hated) -30 好感度

| 物品 | 注册名 |
| --- | --- |
| 牛奶咖啡 | `herbalbrews:milk_coffee` |
| 死亡之液 | `society:death_liquid` |

### librarian (维罗妮卡 · 图书管理员)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意服饰 | `#society:clothing` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 古式墨水 | `supplementaries:antique_ink` |
| 任意菜肴 | `#society:dish` |
| 五彩碎片 | `society:prismatic_shard` |
| 乌龙茶 | `herbalbrews:oolong_tea` |
| 阳光珍珠 | `society:sunlit_pearl` |
| Jellie猫咪葡萄酒 | `vinery:jellie_wine` |
| 灵魂茶 | `society:bowl_of_soul` |

#### 一般 (neutral) +10 好感度

| 物品 | 注册名 |
| --- | --- |
| 兔子脚 | `minecraft:rabbit_foot` |
| 珍珠块 | `crabbersdelight:pearl_block` |

#### 讨厌 (disliked) -15 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意红酒 | `#vinery:red_wine` |
| 任意白酒 | `#vinery:white_wine` |

#### 厌恶 (hated) -30 好感度

| 物品 | 注册名 |
| --- | --- |
| 土烟 | `society:tubasmoke_stick` |
| 土烟烟盒 | `society:tubasmoke_carton` |

### witch (伊芙琳 · 女巫)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意神秘物品 | `#society:eldritch` |
| 能量滋补水 | `society:energy_drink` |
| 粉色能量滋补水 | `society:pink_energy_drink` |
| 白色能量滋补水 | `society:white_energy_drink` |
| 魔力能量滋补水 | `society:mana_energy_drink` |
| 拿铁 | `society:latte` |
| 摩卡 | `society:mocha` |
| 灵魂茶 | `society:bowl_of_soul` |
| 牛奶咖啡 | `herbalbrews:milk_coffee` |
| 榛子咖啡 | `herbalbrews:hazelnut_coffee` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意矿产 | `#society:mineral` |
| 任意花 | `#minecraft:flowers` |
| 咖啡 | `herbalbrews:coffee` |
| 浓缩咖啡 | `society:espresso` |
| 脏柴茶 | `society:dirty_chai` |
| 死亡之液 | `society:death_liquid` |

#### 一般 (neutral) +10 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意农产品 | `#society:farmer_product` |

#### 讨厌 (disliked) -15 好感度

| 物品 | 注册名 |
| --- | --- |
| 松露茶 | `society:truffle_tea` |

#### 厌恶 (hated) -30 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意鱼 | `#minecraft:fishes` |
| 女巫帽 | `herbalbrews:witch_hat` |

### trader (卡洛斯 · 交易商)

#### 最爱 (loved) +40 好感度

| 物品 | 注册名 |
| --- | --- |
| 星椰酒 | `society:star_coquito` |
| 星卡迪 | `society:starcardi` |
| 松露茶 | `society:truffle_tea` |
| 蔬菜配米饭 | `veggiesdelight:rice_and_vegetables` |
| 鸡肉玉米饼汤 | `society:chicken_tortilla_soup` |

#### 喜欢 (liked) +25 好感度

| 物品 | 注册名 |
| --- | --- |
| 霜冻的绒毛 | `snuffles:frosty_fluff` |
| 任意矿产 | `#society:mineral` |
| 任意菜肴 | `#society:dish` |
| 五彩碎片 | `society:prismatic_shard` |
| 兔子脚 | `minecraft:rabbit_foot` |
| 阳光珍珠 | `society:sunlit_pearl` |
| 珍珠块 | `crabbersdelight:pearl_block` |

#### 一般: 无

#### 讨厌 (disliked) -15 好感度

| 物品 | 注册名 |
| --- | --- |
| 任意服饰 | `#society:clothing` |

#### 厌恶 (hated) -30 好感度

| 物品 | 注册名 |
| --- | --- |
| 侏儒 | `society:gnome` |
| 蜘蛛丝 | `society:spider_silk` |

## 特殊 NPC

### wise_oak (智慧橡树)

- **不收任何礼物**。送礼会被拒绝。
- 手持 `树液采集器` (`society:tapper`) 或 `自动树液采集器` (`society:auto_tapper`) 右键会将其好感重置为 0。