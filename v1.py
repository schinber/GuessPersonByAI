"""
机械化的猜人游戏
"""
import random
from typing import List, Dict


class GuessWhoGame:
    def __init__(self):
        self.characters = self.load_characters()
        self.score = 0
        self.max_questions = 10

    def load_characters(self) -> List[Dict]:
        """加载角色数据库"""
        characters = [
            {"name": "爱因斯坦", "category": "科学家", "gender": "男", "hints": ["相对论", "物理学家", "德国出生", "诺贝尔奖"]},
            {"name": "李白", "category": "诗人", "gender": "男", "hints": ["唐代", "诗仙", "饮酒作诗", "蜀地出生"]},
            {"name": "孙悟空", "category": "虚构角色", "gender": "男", "hints": ["西游记", "齐天大圣", "金箍棒", "花果山"]},
            {"name": "居里夫人", "category": "科学家", "gender": "女", "hints": ["放射性研究", "波兰出生", "两次诺贝尔奖", "镭元素"]},
            {"name": "秦始皇", "category": "历史人物", "gender": "男", "hints": ["统一六国", "第一个皇帝", "修建长城", "兵马俑"]},
            {"name": "哈利波特", "category": "虚构角色", "gender": "男", "hints": ["霍格沃茨", "闪电疤痕", "魔法师", "罗琳创作"]},
        ]
        return characters

    def start_game(self):
        print("🎮 欢迎来到猜人游戏！")
        print("我会想一个人物，你可以问问题来猜，或者直接猜名字。")
        print("输入 '提示' 获取提示，'退出' 结束游戏\n")

        self.play_round()

    def play_round(self):
        character = random.choice(self.characters)
        hints_used = 0
        questions_asked = 0

        print(f"🤔 我已经想好了一个{character['category']}人物，开始猜吧！")

        while questions_asked < self.max_questions:
            user_input = input("\n你的问题或猜测: ").strip()

            if user_input.lower() in ['退出', 'exit', 'quit']:
                print(f"游戏结束！正确答案是: {character['name']}")
                break
            elif user_input == '提示':
                if hints_used < len(character['hints']):
                    print(f"💡 提示{hints_used + 1}: {character['hints'][hints_used]}")
                    hints_used += 1
                else:
                    print("没有更多提示了！")
                continue

            # 处理性别相关问题
            if "女" in user_input and ("是" in user_input or "女" in user_input):
                if character['gender'] == '女':
                    print("✅ 是的，这个人物是女性")
                else:
                    print("❌ 不是的，这个人物不是女性")
                questions_asked += 1
                continue

            if "男" in user_input and "是" in user_input:
                if character['gender'] == '男':
                    print("✅ 是的，这个人物是男性")
                else:
                    print("❌ 不是的，这个人物不是男性")
                questions_asked += 1
                continue

            # 检查是否直接猜名字
            if character['name'] in user_input or user_input == character['name']:
                self.score += 1
                print(f"🎉 恭喜你猜对了！就是 {character['name']}")
                print(f"当前得分: {self.score}")
                play_again = input("再来一局？(y/n): ")
                if play_again.lower() == 'y':
                    self.play_round()
                else:
                    print(f"最终得分: {self.score}")
                break
            else:
                # 这里可以集成大模型的问答功能
                print(f"❌ 不对！你还可以问 {self.max_questions - questions_asked - 1} 个问题")
                questions_asked += 1

        if questions_asked >= self.max_questions:
            print(f"❌ 机会用完了！正确答案是: {character['name']}")
            self.show_character_info(character)

    def show_character_info(self, character: Dict):
        print(f"\n📖 人物信息:")
        print(f"姓名: {character['name']}")
        print(f"类别: {character['category']}")
        print(f"性别: {character['gender']}")
        print("提示线索:")
        for hint in character['hints']:
            print(f"  • {hint}")


# 运行游戏
if __name__ == "__main__":
    game = GuessWhoGame()
    game.start_game()
