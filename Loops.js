// for loop

for (i=1;i<=5;i++){
    console.log(i)
}
    

// while loop

let i = 1

while(i>=5){
    console.log(i)
    i++
}

let correctpassword = "abdi123"
let attempts = 0
let isloggin = false

while (attempts < 3 & !isloggin){
    let userpasswrd = prompt("enter you password: ")
    if (userpasswrd == correctpassword){
        console.log("loging seccessfully")
        isloggin = true
    }else{
        attempts++,
        console.log("incorect password you have",3 - attempts, "atttempts letter")
    }
}    
    


if (!isloggin){
    console.log("sorry you lose 3 attemps pls try again leter")
}