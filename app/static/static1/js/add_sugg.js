
function save_sugg() {
    var type= document.getElementById('workfield').value;
    var sugg=document.getElementById('suggest1').value;
    if(sugg.length > 0){
        fetch("/add-sugg",{
            body: JSON.stringify({ type: type, sugg: sugg}),
            method: "POST",
        });
        $('#sid').attr('class','collapse');
        $('#typeofwork').val('')
    }
    else{
        alert("suggestion is empty");
    }
}
function show_sugg() {
    var select = document.getElementById('sugg');
    const value = select.options[select.selectedIndex].value;
     
}
function mg(){
    var lat=document.getElementById('lat').value;
    var select = document.getElementById('select_city');
    const value = select.options[select.selectedIndex].value;
    if(value.length == 0){
        alert("Select city");
        return false;
    }
    else if(lat.length == 0){
        alert("Choose your current Location");
        return false;
    }
    else{
        return true;
    }
}