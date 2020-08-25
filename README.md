# git-measure
Measure length of tex file over time. Crashes if any commit text contains the word commit

If macOS X Catalina 10.15.6, add
- ""
after
- "sed -i",
i.e.
- sed -i "" '$d' .gitattributes
