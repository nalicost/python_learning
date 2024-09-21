"""
            技能的设计与生成
"""
#以下类都体现单一原则
"""
三大特征：1、封装：DizzinessEffect、DamageEffect、DefenceIncreaseEffect、CatchAttentionEffect封装具体
        效果，SkillEffectManager封装具体技能
        2、继承：SkillEffect继承DizzinessEffect、DamageEffect、DefenceIncreaseEffect、CatchAttentionEffect
        3、多态：调用SkillEffect的impact方法，实际执行的是子类的具体impact方法
六大原则：1、开闭原则：增加新的效果或者技能不修改解释器代码
        2、单一职责：SkillEffect负责隔离变化，DizzinessEffect、DamageEffect、DefenceIncreaseEffect、CatchAttentionEffect负责具体
        效果，SkillEffectManager负责生成技能
        3、依赖倒置：DizzinessEffect、DamageEffect、DefenceIncreaseEffect、CatchAttentionEffect依赖SkillEffect，统一概念
                   SkillEffect不依赖于DizzinessEffect、DamageEffect、DefenceIncreaseEffect、CatchAttentionEffect，依赖注入，即
                   通过配置文件来创建效果对象，而不是由SkillEffect创建
        4、组合复用：SkillEffectManager调用SkillEffect而不是直接调用其子类
        5、里氏原则：子类impact重写父类impact
        6、迪米特法则：组织松散，耦合度低
"""


class SkillEffect:
    def impact(self):
        # 多态，实现技能个性效果，开闭原则，依赖倒置原则
        raise NotImplementedError


class DizzinessEffect(SkillEffect):
    # 继承技能影响
    def __init__(self, time):
        self.time = time

    def impact(self):
        # 里氏替换原则
        print(f'眩晕{self.time}秒')


class DamageEffect(SkillEffect):
    # 继承技能影响
    def __init__(self, damage, attack_num):
        self.damage = damage
        self.attack_num = attack_num

    def impact(self):
        # 里氏替换原则

        print(f'攻击{self.attack_num}个人，扣他{self.damage}血')


class DefenceIncreaseEffect(SkillEffect):
    # 继承技能影响
    def __init__(self, defence_increase, time):
        self.defence_increase = defence_increase
        self.time = time

    def impact(self):
        # 里氏替换原则

        print(f'防御力提升{self.defence_increase}，持续{self.time}秒')


class CatchAttentionEffect(SkillEffect):
    def __init__(self, impact_range, time):
        self.impact_range = impact_range
        self.time = time

    def impact(self):
        # 里氏替换原则

        print(f'嘲讽{self.impact_range}个最近单位，持续{self.time}秒')


class SkillEffectManager:
    skill_effect = SkillEffect()

    def __init__(self, name):
        # 封装技能效果与技能名字
        self.name = name
        skill_dict_config = self.get_skills_config()
        self.skill_effect_list = self.get_skill_config(skill_dict_config)

    def get_skills_config(self):
        return {"狮吼功": [DizzinessEffect(5), DamageEffect(100, 10)]}

    def get_skill_config(self, skill_dict):
        return skill_dict[self.name]

    def affect_skill(self):
        for skill_effect in self.skill_effect_list:
            # 组合复用，跨类调用技能效果方法
            skill_effect.impact()


shg = SkillEffectManager('狮吼功')
shg.affect_skill()
