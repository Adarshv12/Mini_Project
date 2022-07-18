const user_search=document.querySelector("#user_search");

const tableOutput=document.querySelector(".table_output");
tableOutput.style.display = "none";
const tbody=document.querySelector(".table-body");
function filter(){
    var chbox_type=document.getElementById("type");
    var chbox_place=document.getElementById("place");
    var chbox_pin=document.getElementById("pin");
    user_search.addEventListener('keyup',(e)=>{
        const searchvalue = e.target.value;

        if(chbox_type.checked == true){
            if(searchvalue.trim().length > 0){
                console.log("searchvalue",searchvalue);
                tbody.innerHTML="";
                fetch("/search-type",{
                    body: JSON.stringify({ searchtxt: searchvalue }),
                    method: "POST",
                })
                .then((res) => res.json())
                .then((data) => {
                    console.log("data",data);

                    tableOutput.style.display = "block";
                    if(data.length === 0){

                    }
                    else{
                        data.forEach((item) => {
                            tbody.innerHTML += `
                            <tr>
                            <td><img src="${item.profile_image}" height="50" width="50"></td>
                            <td> ${item.U_name}</td>
                            <td> ${item.city}</td>
                            <td> ${item.pincode}</td>
                            <td> ${item.Fd_of_work}</td>
                            <input type="hidden" id="${item.Worker_id}">
                            <td> <button href="#" class="btn btn-primary" data-toggle="collapse" data-target="#sid" id="click" onclick="return inviteform(document.getElementById('${item.Worker_id}').id)"> Invite </button></td>
                            </tr>`
                        });
                    }
                });
            }
            else{
                tbody.innerHTML="";
                tableOutput.style.display = "none";
            }
        }
        else{
            tbody.innerHTML="";
            tableOutput.style.display = "none";
        }


        if(chbox_place.checked == true){
            if(searchvalue.trim().length > 0){
                console.log("searchvalue",searchvalue);
                tbody.innerHTML="";
                fetch("/search-place",{
                    body: JSON.stringify({searchtxt: searchvalue}),
                    method: "POST",
                })
                .then((res) => res.json())
                .then((data) => {
                    console.log("data",data);

                    tableOutput.style.display = "block";
                    if(data.length === 0){

                    }
                    else{
                        data.forEach((item) => {
                            tbody.innerHTML += `
                            <tr>
                            <td><img src="${item.profile_image}" height="50" width="50"></td>
                            <td> ${item.U_name}</td>
                            <td> ${item.city}</td>
                            <td> ${item.pincode}</td>
                            <td> ${item.Fd_of_work}</td>
                            <input type="hidden" id="${item.Worker_id}">
                            <td> <button href="#" class="btn btn-primary" data-toggle="collapse" data-target="#sid" id="click" onclick="return inviteform(document.getElementById('${item.Worker_id}').id)"> Invite </button></td>
                            </tr>`
                        });
                    }
                });
            }
            else{
                tbody.innerHTML="";
                tableOutput.style.display = "none";
            }
        }
        else{
            tbody.innerHTML="";
            tableOutput.style.display = "none";
        }

        if(chbox_pin.checked == true){
            if(searchvalue.trim().length > 0){
                console.log("searchvalue",searchvalue);
                tbody.innerHTML="";
                fetch("/search-pin",{
                    body: JSON.stringify({searchtxt: searchvalue}),
                    method: "POST",
                })
                .then((res) => res.json())
                .then((data) => {
                    console.log("data",data);

                    tableOutput.style.display = "block";
                    if(data.length === 0){

                    }
                    else{
                        data.forEach((item) => {
                            tbody.innerHTML += `
                            <tr>
                            <td><img src="${item.profile_image}" height="50" width="50"></td>
                            <td> ${item.U_name}</td>
                            <td> ${item.city}</td>
                            <td> ${item.pincode}</td>
                            <td> ${item.Fd_of_work}</td>
                            <input type="hidden" id="${item.Worker_id}">
                            <td> <button href="#" class="btn btn-primary" data-toggle="collapse" data-target="#sid" id="click" onclick="return inviteform(document.getElementById('${item.Worker_id}').id)"> Invite </button></td>
                            </tr>`
                        });
                    }
                });
            }

            else{
                tbody.innerHTML="";
                tableOutput.style.display = "none";
            }
        }
        else{
            tbody.innerHTML="";
            tableOutput.style.display = "none";
        }
    });
}
function inviteform(id){
    document.getElementById('user_search').value='';
    tableOutput.style.display = "none";
    console.log("id",id);
    fetch("/get-worker_id",{
        body: JSON.stringify({searchtxt: id}),
        method: "POST",
    })
    .then((res) => res.json())
    .then((data) =>{
        console.log("data",data);
        data.forEach((item) => {
            document.getElementById('city1').value=item.city;
            document.getElementById('type1').value=item.Fd_of_work;
            document.getElementById('wid1').value=item.Worker_id;
            document.getElementById('wname').value=item.U_name;
            

        })

    });
    

}