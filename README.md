# nqasm

This is a visual studio code syntax highlighter and auto completer for the newserv quest script assembler, for phantasy star online.
<img width="1064" height="770" alt="image" src="https://github.com/user-attachments/assets/58d83efe-bddc-4332-b580-1e89d29ae950" />



# How to install

1. Download the latest release from the releases section.

2. Click the extensions tab.

   <img width="43" height="291" alt="image" src="https://github.com/user-attachments/assets/3f75ad57-c011-402f-a794-741080c7784b" />
   
3. Click the 3 dots above the extensions search bar.
  <img width="339" height="83" alt="image" src="https://github.com/user-attachments/assets/7ef9a374-3f0d-40d1-8328-044dde2962e6" />

4. Click install from vsix and select the "nqasm-x.x.x.vsix" that you downloaded from releases.

5. (Optional) Click the gear on the nqasm extension, then click "set theme" to use the theme I made for nqasm.
   <img width="409" height="148" alt="image" src="https://github.com/user-attachments/assets/2c3eb17e-b32f-4b72-9261-f85de23fe934" />

# How to use

Probably goes without saying that you need a release of [newserv](https://github.com/fuzziqersoftware/newserv/) downloaded to use this.

1. Download NqasmScriptTemplate.txt from above

2. In visual studio code open NqasmScriptTemplate.txt

3. At the very bottom of visual studio code click where it says "{} Plain Text"
   
   <img width="173" height="36" alt="image" src="https://github.com/user-attachments/assets/b725366d-3331-4b75-a1d1-c7fbc656bfc5" />

4. Select nqasm from the list of languages
   
5. Once you're done editing your quest script, open a command prompt and run the following command: <newserv.exe location> assemble-quest-script --bb <questscript.txt location> (replace --bb with the pso version you're making the quest for)

6. Your assembled quest script will be in the same folder as your non-assembled questscript.txt

# Resources

An example of a complete quest script that shows off most of the newserv script assembler's abilities can be found here in [newserv's repository](https://github.com/fuzziqersoftware/newserv/blob/master/system/quests/retrieval/q058-gc-e.bin.txt).

You can find the list of quest script opcodes here in [newserv's code](https://github.com/fuzziqersoftware/newserv/blob/master/src/QuestScript.cc#L334).

There's also a list of opcodes on the [qedit wiki](https://www.qedit.info/index.php?title=Main_Page) and other things related to creating quests.

If you need help debugging your script or have questions about quest creation in general, the people in the [qedit discord](https://discord.com/invite/Ww2G9Zb) can help.
