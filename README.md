### GGUF model caller

[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/callgg.gif" width="128" height="128">](https://github.com/calcuis/chatgpt-model-selector/blob/main/callgg.gif)
[![Static Badge](https://img.shields.io/badge/callgg-release-yellow?logo=github)](https://github.com/calcuis/callgg/releases)

This package is a GGUF (GPT-Generated Unified Format) file/model caller.
#### install the caller via pip/pip3 (once only):
```
pip install callgg
```
#### update the caller (if not in the latest version) by:
```
pip install callgg --upgrade
```
### user manual
This is a cmd-based (command line) package, you can find the user manual by adding the flag -h or --help.
```
callgg -h
```
#### call gguf-selector for running a GGUF model/file:
```
callgg run
``` 

GGUF file(s) in the same directory will automatically be detected by the caller, hence, a selection menu will be shown in the console as below.

[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo.gif)
[<img src="https://raw.githubusercontent.com/calcuis/chatgpt-model-selector/master/demo1.gif" width="350" height="280">](https://github.com/calcuis/chatgpt-model-selector/blob/main/demo1.gif)

#### sample model(s) available to download (try out)
For general purpose
[chat.gguf] (file size: around 2GB or less)
```
callgg save https://huggingface.co/calcuis/chat/resolve/main/chat.gguf
```
For coding
[code.gguf] (file size: around 3GB or more)
```
callgg save https://huggingface.co/calcuis/chat/resolve/main/code.gguf
```
For health/medical advice
[medi.gguf] (file size: around 3GB or more)
```
callgg save https://huggingface.co/calcuis/chat/resolve/main/medi.gguf
```
***those are all experimental models; no guarantee on quality
