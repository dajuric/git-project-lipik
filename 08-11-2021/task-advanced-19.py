strXml = """
<!DOCTYPE html>
<html>
<head>
    <title>Naslov stranice</title>
    <script>
        /*neki javascript kod na primjer*/
    </script>
    <link rel="stylesheet" href="css/styles.css">
</head>

<body>
   <h1>
      Ovo je moj prvi susret sa HTML-om
   </h1>
   <p class="uppercase">
      HTML nije programski jezik.
   </p>
</body>
</html>
"""
import re

stack = []
nonContainingTags = ["link"]

i = 0
while i < len(strXml):
    openTagMatch = re.search("\<(\w+).*?\>", strXml[i:], re.M) #match open tag and its attributes
    closeTagMatch = re.search("\<\/(\w+)>", strXml[i:], re.M) #match close tag 

    tagMatch = openTagMatch
    isOpen = True

    if openTagMatch == None and closeTagMatch == None:
        break

    if openTagMatch == None or openTagMatch.start() > closeTagMatch.start(): 
        tagMatch = closeTagMatch
        isOpen = False

    tag = tagMatch.group(1)
    if isOpen:
        if tag not in nonContainingTags:
            stack.append(tag)
    else:
        if tag == stack[-1]:
            stack.pop()
        else:
            print(f"The expected closing tag is: {stack[-1]}, but received: {tag}!")
            break

    i += tagMatch.end()

print("HTML is valid" if len(stack) == 0 else f"HTML contains unclosed tags: {print(stack)}.")
