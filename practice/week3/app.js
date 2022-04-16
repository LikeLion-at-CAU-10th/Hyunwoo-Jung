//const checkbox =document.getElementById("checkbox");
const checkbox = document.querySelector('.checkbox');

checkbox.addEventListener('click',click);

function click(){
    if(document.body.classList.contains('dark')){
        document.body.classList.remove('dark');
        console.log("convert into Light Mode");
        
    }else{
        document.body.classList.add('dark');
        console.log("convert into Dark Mode");
    }
}




