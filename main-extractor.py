# a gui phones\emails extractor
import re
# the phone regex :
PhoneRe = re.compile(r'''( 
#555-555-1234 or 555-1234 or (555)-555-1234 << american numbers examples
(((\d\d\d) | (\(\d\d\d\)))? # d meaning digit | meaning or ? meaning optional and (meaning group)
(\s|-)   #seprators \s mean space and - mean - LOL kidding with you bro
\d\d\d   #first three digits
-        #another separators
\d\d\d\d\s)? #last digits \s means space
((\d\d\d)?(-)?(0?\d{9}))? # this is regex for arabs countries code \d{9} short cut for \d\d\d\d\d\d\d\d\d
)''',re.VERBOSE)
#VERBOSE for writing commends inside the triple quotations
# re.compile('((\d\d\d) | (\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d') without verbose mode

# emails regex :
EmailRe = re.compile(r''' 
# anything@anything.anything << emails examples 
[A-Za-z0-9_.+]+ #name part [create our own regex A-Z all capital letters a-z all small letters _+ some symbols]
@                # @ symbol
[A-Za-z0-9_.+]+ # domain part the last (+) means must has something after it like .com or .net
''', re.VERBOSE)

text = ('''
blskdjskjfsjfjvij 0501024226 and sjjhewusdhiheuhduhsi 966501024226 saijiuhaiuhdsyuhwbauidhsuiha
504-925-2032 
Howard Palmer  palme7345@live.com  984-739-5933

''') # paste your text here

ExtractedP = PhoneRe.findall(text) # findall means start collecting the regex
ExtractedE = EmailRe.findall(text)
#print(ExtractedP)

# findall return list of tuples so that why we create this loop try the code without this loop to understand from here
EveryPhone = []
for phone in ExtractedP:
    EveryPhone.append(phone[0])
# to here and don't forget to print ExtractedP not EveryPhone
#print(EveryPhone)
# all this to print it in a good format don't be scare
final = ("phones\n-------------\n"+"\n".join(EveryPhone) + "\nemails\n-------------------\n" +"\n".join(ExtractedE))
final =final.split()

print("\n".join(final))