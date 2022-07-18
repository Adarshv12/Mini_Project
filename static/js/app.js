const formSelector = document.getElementById("roll_selector");

const formType = document.getElementById("main_form");

const customerForm = `

<form action="/customer_registration/" method="post" class="tm-signup-form" name="f">

<div class="input-field">
    <input placeholder="Name"  name="Name" type="text" class="validate" required="">
</div>

<div class="input-field">
    <input placeholder="Username" name="username" type="text" class="validate" required="">
</div>
<div class="input-field">
    <input placeholder="Address" name="Address" type="text" class="validate" required="">
</div>
<div class="input-field">
    <input placeholder="Phone NO" name="phno" type="text" class="validate" required="">
</div>
<div class="input-field">
    <input placeholder="Email ID" name="email" type="text" class="validate" required="">
</div>
<div class="input-field">
    <input placeholder="Password" name="password" type="password" class="validate" id="myinput" required="">
</div>
<div class="input-field">
    <input placeholder="Re-type Password" name="password2" type="password" class="validate" required="">
</div>

<div class="text-right mt-4">
    <button type="submit" class="waves-effect btn-large btn-large-white px-4 tm-border-radius-0" onclick="return mg()">Sign Up</button>
</div>
</form>`;

const contractorForm = `
<form action="/contractor_registration/" method="post" class="tm-signup-form" name="f">
                    {% csrf_token %}
                    <div class="input-field">
                        <input placeholder="Name"  name="Name" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Username" name="username" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Address" name="Address" type="text" class="validate" required="">
                    </div>
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
                            <select name="city">
                                <option value="-">Your City</option>
                                <option value="Bangkok">Calicut</option>
                                <option value="Yangon">Kottayam</option>
                                <option value="Mumbai">Kochi</option>
                                <option value="Singapore">Trivandrum</option>
                            </select>
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pr-0 tm-pl-xs-0">
                            <div class="input-field">
                                <input placeholder="Zip Code" id="zipcode" name="zipcode" type="text" class="validate">
                            </div>
                        </div>
                    </div>
                    <div class="input-field">
                        <input placeholder="Phone NO" name="phno" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Email ID" name="email" type="text" class="validate" required="">
                    </div>
                    <div class="row">
                        <select name="fd_of_work" required="">
                            <option value="-">Field of Work</option>
                            <option value="Borewell">Borewell</option>
                            <option value="Carpentry">Carpentry</option>
                            <option value="Carpet">Carpet</option>
                            <option value="Construction">Construction</option>
                            <option value="Drainage">Drainage</option>
                            <option value="Drilling">Drilling</option>
                            <option value="Electrical">Electrical</option>
                            <option value="Elevator">Elevator</option>
                            <option value="Fabrication">Fabrication</option>
                            <option value="False Ceiling">False Ceiling</option>
                            <option value="Fire Fighting">Fire Fighting</option>
                            <option value="Flooring">Flooring</option>
                            <option value="Furniture">Furniture</option>
                            <option value="Gardening">Gardening</option>
                            <option value="Interior">Interior</option>
                            <option value="Painting">Painting</option>
                            <option value="Pipeline">Pipeline</option>
                            <option value="Plumbing">Plumbing</option>
                            <option value="Swimming Pool">Swimming Pool</option>
                            <option value="Wall Paper">Wall Paper</option>
                            <option value="Waterproofing">Waterproofing</option>
                            <option value="Welding">Welding</option>
                            <option value="-">Other</option>
                        </select>
                    </div>
                    <BR>
                    <!-- <div class="input-field">
                        <input placeholder="Field of Work" name="fd_of_work" type="text" class="validate" required="">
                    </div> -->
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
                            <input placeholder="Experience(years)" name="exp" type="text" class="validate" required="">
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
                            <select name="expm">
                                <option value="-">Months</option>
                                <option value="0">0</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                                <option value="6">6</option>
                                <option value="7">7</option>
                                <option value="8">8</option>
                                <option value="9">9</option>
                                <option value="10">10</option>
                                <option value="11">11</option>
                                <option value="12">12</option>
                            </select>
                        </div>
                    </div>
                    <!-- <div class="input-field">
                        <input placeholder="Experience" name="exp" type="text" class="validate" required="">
                    </div> -->

                    <div class="input-field">
                        <input placeholder="License NO (optional)" name="lic_no" type="text" class="validate">
                    </div>
                    <div class="input-field">
                        <input placeholder="Password" name="password" type="password" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Re-type Password" name="password2" type="password" class="validate" required="">
                    </div>
                    
                    <div class="text-right mt-4">
                        <button type="submit" class="waves-effect btn-large btn-large-white px-4 tm-border-radius-0" onclick="return mg()">Sign Up</button>
                    </div>
                </form>`;

const companyForm = `
<form action="/company_registration/" method="post" class="tm-signup-form" name="f">
                    {% csrf_token %}
                    <div class="input-field">
                        <input placeholder="Company Name"  name="Name" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Username" name="username" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Address" name="Address" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Phone NO" name="phno" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Email ID" name="email" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="License NO" name="lic_no" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Password" name="password" type="password" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Re-type Password" name="password2" type="password" class="validate" required="">
                    </div>
                    
                    <div class="text-right mt-4">
                        <button type="submit" class="waves-effect btn-large btn-large-white px-4 tm-border-radius-0" onclick="return mg()">Sign Up</button>
                    </div>
                </form>`;
const workerForm = `
<form action="/worker_registration/" method="post" class="tm-signup-form" name="f">
                    {% csrf_token %}
                    <div class="input-field">
                        <input placeholder="Name"  name="Name" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Username" name="username" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Address" name="Address" type="text" class="validate" required="">
                    </div>
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
                            <select name="city">
                                <option value="-">Your City</option>
                                <option value="Bangkok">Calicut</option>
                                <option value="Yangon">Kottayam</option>
                                <option value="Mumbai">Kochi</option>
                                <option value="Singapore">Trivandrum</option>
                            </select>
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pr-0 tm-pl-xs-0">
                            <div class="input-field">
                                <input placeholder="Zip Code" id="zipcode" name="pincode" type="text" class="validate">
                            </div>
                        </div>
                    </div>
                    <div class="input-field">
                        <input placeholder="Phone NO" name="phno" type="text" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Email ID" name="email" type="text" class="validate" required="">
                    </div>
                    <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
                        <select name="fd_of_work">
                            <option value="-">Field of Work</option>
                            <option value="Borewell">Borewell</option>
                            <option value="Carpentry">Carpentry</option>
                            <option value="Carpet">Carpet</option>
                            <option value="Construction">Construction</option>
                            <option value="Drainage">Drainage</option>
                            <option value="Drilling">Drilling</option>
                            <option value="Electrical">Electrical</option>
                            <option value="Elevator">Elevator</option>
                            <option value="Fabrication">Fabrication</option>
                            <option value="False Ceiling">False Ceiling</option>
                            <option value="Fire Fighting">Fire Fighting</option>
                            <option value="Flooring">Flooring</option>
                            <option value="Furniture">Furniture</option>
                            <option value="Gardening">Gardening</option>
                            <option value="Interior">Interior</option>
                            <option value="Painting">Painting</option>
                            <option value="Pipeline">Pipeline</option>
                            <option value="Plumbing">Plumbing</option>
                            <option value="Swimming Pool">Swimming Pool</option>
                            <option value="Wall Paper">Wall Paper</option>
                            <option value="Waterproofing">Waterproofing</option>
                            <option value="Welding">Welding</option>
                            <option value="-">Other</option>
                        </select>
                    </div>
                    <!-- <div class="input-field">
                        <input placeholder="Field of Work" name="fd_of_work" type="text" class="validate" required="">
                    </div> -->
                    <div class="row">
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
                            <input placeholder="Experience(years)" name="exp" type="text" class="validate" required="">
                        </div>
                        <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-6 pl-0 tm-pr-xs-0">
                            <select name="expm">
                                <option value="-">Months</option>
                                <option value="0">0</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                                <option value="6">6</option>
                                <option value="7">7</option>
                                <option value="8">8</option>
                                <option value="9">9</option>
                                <option value="10">10</option>
                                <option value="11">11</option>
                                <option value="12">12</option>
                            </select>
                        </div>
                    </div>
                    <!-- <div class="input-field">
                        <input placeholder="Experience" name="exp" type="text" class="validate" required="">
                    </div> -->
                    <div class="input-field">
                        <input placeholder="Password" name="password" type="password" class="validate" required="">
                    </div>
                    <div class="input-field">
                        <input placeholder="Re-type Password" name="password2" type="password" class="validate" required="">
                    </div>
                    
                    <div class="text-right mt-4">
                        <button type="submit" class="waves-effect btn-large btn-large-white px-4 tm-border-radius-0" onclick="return mg()">Sign Up</button>
                    </div>
                </form>
`;
let value = "student"

    formType.innerHTML = customerForm;

formSelector.addEventListener('change', function() {
    value = document.forms[0].roll_selector.value;
    
    if(value === ""){
      alert("Please select your roll")
      formType.innerHTML = "";
    }else if(value === "customer"){
      formType.innerHTML = customerForm;
    }else if(value === "contractor"){
      formType.innerHTML = contractorForm;
    }else if(value === "company"){
      formType.innerHTML = companyForm;
    }else if(value === "worker"){
        formType.innerHTML = workerForm;
    }

});