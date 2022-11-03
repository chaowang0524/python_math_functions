import re
content = """adarstat 12345@qq.com arstnooaeirsnt
arstarstazxvcasdf 12dsa#abc.com addoneia
fF python666@163.cn #: H8
*TifF, l python-abc@163com *#.
R# python_ant-666@sina.net Hl#,"""

result = re.findall(r' (.+@.+\.\w+) ', content)
print(result)

# standard format for an email address
"""[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}"""
