s = """The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
s1 = s.replace('better','worse')
print(s1)
word_str = s1.replace(',','').replace('.','').replace('!','').replace('*','').replace('--','')
word_list = word_str.split()
y=[]
for word in word_list:
    if word.find('ea') < 1:
        y.append(word)

s2 = ' '.join(y)

print(s2)
s3 = s2.swapcase()
print(s3)
s4 = s3.split()
s4.sort()
print(s4)