# GrammerAPI (My code is bad)
The heroku instance may sleep so it may take a while to reply  
A grammar fixer that uses AI to fix stuff  
POST raw data to https://grammarapi.herokuapp.com/  

Models download at the deepcorrect github  
Credit:
  https://github.com/bedapudi6788/deepcorrect
  https://github.com/bedapudi6788/deepsegment

Basic Function:
```
async function grammarapi(str) {
    let r = await fetch('https://grammarapi.herokuapp.com', {
        method: 'POST',
        body: str
    })
    return r.text();
}
```
To use:
```grammarapi("hi").then(a => console.log(a))```
