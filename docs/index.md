# Homepage

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Code Annotation Examples

### Codeblocks

Some `code` goes here.

### Plain codeblock

A plain codeblock:

```py
Some code here
text = 'Hello, my name is [u-1061][u-1072][u-1082][u-1080]!'

for i in range(64):
    Unicode = ord('А')+i
    if str(Unicode) in text:
        text = text.replace(f'[u-{Unicode}]', chr(Unicode))


print(text)


```