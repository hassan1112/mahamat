
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Housing price prediction</title>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<style type="text/css">
.register{
    background: -webkit-linear-gradient(left, #3931af, #00c6ff);
    margin-top: 3%;
    padding: 3%;
}
body {
    background-image:{{ img }};
    background-repeat: no-repeat;
    background-size: cover;
  
    background-color: #007a99;
}
.register-left{
    text-align: center;
    color: #fff;
    margin-top: 4%;
}
.register-left input{
    border: none;
    border-radius: 1.5rem;
    padding: 2%;
    width: 60%;
    background: #f8f9fa;
    font-weight: bold;
    color: #383d41;
    margin-top: 30%;
    margin-bottom: 3%;
    cursor: pointer;
}
.register-right{
    background: #f8f9fa;
    border-top-left-radius: 10% 50%;
    border-bottom-left-radius: 10% 50%;
}
.register-left img{
    margin-top: 15%;
    margin-bottom: 5%;
    width: 25%;
    -webkit-animation: mover 2s infinite  alternate;
    animation: mover 1s infinite  alternate;
}
@-webkit-keyframes mover {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
}
@keyframes mover {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
}
.register-left p{
    font-weight: lighter;
    padding: 12%;
    margin-top: -9%;
}
.register .register-form{
    padding: 10%;
    margin-top: 10%;
}
.btnRegister{
    margin-left: -70px;
    margin-top: 10%;
    border: none;
    border-radius: 0.5rem;
    padding: 2%;
    background: #0062cc;
    color: #fff;
    font-weight: 600;
    width: 50%;
    cursor: pointer;
}
.register .nav-tabs{
    margin-top: 3%;
    border: none;
    background: #0062cc;
    border-radius: 1.5rem;
    width: 28%;
    float: right;
}
input:invalid {
    border-color: red;
}
input,
input:valid {
    border-color: #ccc;
}

h3 {
    font-family: sans-serif;
    font-size: 36px;
    font-style: bold;
    color: red;
   }

#para {
    font-size: 20px;
    
}
.register .nav-tabs .nav-link{
    padding: 2%;
    height: 34px;
    font-weight: 600;
    color: #fff;
    border-top-right-radius: 1.5rem;
    border-bottom-right-radius: 1.5rem;
}
.register .nav-tabs .nav-link:hover{
    border: none;
}
.register .nav-tabs .nav-link.active{
    width: 100px;
    color: #0062cc;
    border: 2px solid #0062cc;
    border-top-left-radius: 1.5rem;
    border-bottom-left-radius: 1.5rem;
}
.register-heading{
    text-align: center;
    margin-top: 8%;
    margin-bottom: -15%;
    color: #495057;
}
#result 
{
margin-left: 20px;
color: red;
font-size: 25px;
font-style: bold;
}
.result {
font-size: 25px;
font-style: bold;
color: black;
margin-left: 60px;

}
 </style>



<script type="text/javascript">
function validate(){
	var zipcode = Number(document.getElementByid('zipcode').value);
	var pattern = RegExp('/^98[0-9]{3}$/');
    
	if(!pattern.test(zipcode))
	{
     alert("King County zipcode must be of 5 digits and it should start with 98 followed by 3  digits area pin code eg [98012");
	}
}
</script>
</head>
<body>
  <div class="container register">
                <div class="row">
                    
                    <div class="col-md-3 register-left">
                        <img src="img1.png" alt="" width="500" height="100"/>
                        <h1 class="text-primary h1">Welcome  to  </h1>
                        <p id ="para"> Hybrid housing price prediction model</p>
                       
                    </div>
                    
                    <div class="col-md-9 register-right">
                        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
                            <li class="nav-item">
                                <a class="nav-link active" id="home-tab" data-toggle="tab" href="#Buy" role="tab" aria-controls="home" aria-selected="true">Buy</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" id="profile-tab" data-toggle="tab" href="#sale" role="tab" aria-controls="profile" aria-selected="false">Sale</a>
                            </li>
                        </ul>
                        <div class="tab-content" id="myTabContent">
                            <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                                <h3 class="register-heading">Housing price prediction model</h3>
                                <div class="row register-form">
                                    <div class="col-md-6">
                                 <form action='/process' method="POST"> 
                                        <div class="form-group">
                                            <input type="number" class="form-control" placeholder="bedrooms *" name="bedrooms" value="" />
                                        </div>

                                        <div class="form-group">
                                            <input type="number" class="form-control" placeholder="bathrooms *" name="bathrooms" value="" autocomplete="on" />
                                        </div>

                                        <div class="form-group">
                                            <input type="number" class="form-control" placeholder="sqf of living room*" name="sqft_living" value="" autocomplete="on"/>
                                        </div>

                                        <div class="form-group">
                                            <input type="number" class="form-control" placeholder="sqft lot *" name="sqft_lot" value="" autocomplete="on"/>
                                        </div>
                                        
                                        <div class="form-group">
                                            <input type="number" class="form-control" placeholder="how many floors *" name="floors" value="" autocomplete="on"/>
                                        </div>
                                        
                                           <div class="form-group">
                                            <select class="form-control" name="condition" autocomplete="on">
                                                <option class="hidden"  selected disabled>Condition</option>
                                                <option>1</option>
                                                <option>2</option>
                                                <option>3</option>
                                                <option>4</option>
                                                <option>5</option>
                                            </select>
                                        </div>
                                        
                                    </div>
                                    <div class="col-md-6">

                                        <div class="form-group">
                                            <input type="number" class="form-control" placeholder="sqft of above *" name="sqft_above" value="" autocomplete="on"/>
                                        </div>


                                        <div class="form-group">
                                            <input type="text" class="form-control" placeholder="sqft basement *"name="sqft_basement" value="" autocomplete="on" />
                                        </div>

                                        

                                        <div class="form-group">
                                            <input type="text" class="form-control" placeholder="year built *"name="yr_built" value="" autocomplete="on" maxlength="4" />
                                        </div>
                                        <div class="form-group">
                                            <input type="text" class="form-control" placeholder="zipcode eg 98004*" name="zipcode" value="" autocomplete="on" maxlength="5" />
                                        </div>
                                        <div class="form-group">
                                            <input type="text"  maxlength="10" name="lat" class="form-control" placeholder="latitude *" name="lat" value="" autocomplete="on"/>
                                        </div>
                                       
                                        <div class="form-group">
                                            <input type="text" class="form-control" placeholder="Longitude *" name="long" value="" autocomplete="on"/>
                                        </div>

                                       


                                        <input type="submit" class="btnRegister"  value="Predict" onclick="validate();" />
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade show" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                                <h3  class="register-heading">Result</h3>
                                <div class="row register-form">
                                    <div class="col-md-6">
                                    

                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
                <p class ="result">{{ txt }} <span id="result">{{ variable }}</span></p>
                </div>

            </div>
            
            </body>

</html>