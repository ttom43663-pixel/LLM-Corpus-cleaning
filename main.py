import json


max_length = 128


#原始语料
data = []
with open("origional.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data.append(json.loads(line))


#加载屏蔽词
blacklist =[]
with open("FORBIEDN.txt","r",encoding="UTF-8") as f:
    temp = f.readlines()
for a in temp:
    blacklist.append(a.replace("\n",""))


def isHave(data):
    for a in blacklist:
        if a in data:
            return True
    return False


#清洗语料
astr = ""
count = 0
section = {}
with open("final.jsonl","a",encoding="UTF-8") as f:
    for a in range(0, len(data)):
        section = data[a]["conversations"][0]
        if not isHave(data[a]["conversations"][1]["content"]) and(len(data[a]["conversations"][1]["content"])<max_length):
            p1 = section["content"]
            p2 = data[a]["conversations"][1]["content"]
            datapack = {
                "conversations": [
                    {"role": "user", "content": f"{p1}"},
                    {"role": "assistant", "content": f"{p2}"}
                ]
            }
            f.write(json.dumps(datapack, ensure_ascii=False) + "\n")


print(count)