# json格式装换
# 注意文件名不能命名成json.py
import json

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d = json.loads(json_str)
print(d)


# json 进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('小王', 18, 88)


# print(json.dumps(s))  # 报错：原因是Student不是一个可以序列化的对象

# 补充转化函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 得到json数据
print(json.dumps(s, default=student2dict))

# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))  # 同样可以实现序列化


# json反序列为对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str, object_hook=dict2student))  # 得到Student对象

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
s = json.dumps(obj, ensure_ascii=False)
print(s)
'''
{"name": "Bob", "score": 88, "age": 20}
{'name': 'Bob', 'score': 88, 'age': 20}
{"name": "\u5c0f\u738b", "score": 88, "age": 18}
{"name": "\u5c0f\u738b", "age": 18, "score": 88}
<__main__.Student object at 0x000000000122ADA0>
{"name": "\u5c0f\u660e", "age": 20}
{"name": "小明", "age": 20}
'''
