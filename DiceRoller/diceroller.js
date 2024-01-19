
function rolldice(){
    const numofdice = document.getElementById("numofdice").value;
    const diceresult= document.getElementById("diceresult");
    const diceimages = document.getElementById("images");
    const values=[];
    const images=[];
    for(let i=0; i < numofdice; i++){
        const value=Math.floor(Math.random()*6)+1;
        values.push(value);
        images.push(`<img src="${value}.png">`);
    }
    console.log(`dice: ${values.join(', ')}`)
    diceresult.textContent=`dice: ${values.join(', ')}`;
    diceimages.innerHTML= images.join('');
}