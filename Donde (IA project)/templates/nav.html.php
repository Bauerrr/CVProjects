<?php
/** @var $router \App\Service\Router */
/** @var $pracownik ?\App\Model\pracownik */
/** @var $pomieszczenie ?\App\Model\pomieszczenie */

use App\Model\pracownik;

?>
<div>
<ul>
    <li><a href="<?= $router->generatePath('') ?>">Mapa</a></li>


    <li><a id="search" onclick="si()">Szukaj</a></li>


    <li id="liPanel"><a href="<?= $router->generatePath('admin-index') ?>">Panel administratora</a></li>


    <li id="liLogowanie"><a href="<?= $router->generatePath('') ?>">Logowanie</a></li>


    <li id="liUser"><a>Użytkownik |</a></li>


    
</ul>
</div>

<div id="sear" style="z-index: 2" >
</div>
<script>
    let login = '<?php 
    if(isset($_SESSION['login'])){
        echo $_SESSION['login'];
    }
    ?>';
    if(login != ''){
        document.getElementById('liPanel').style.visibility = 'visible';
        let logout = document.getElementById('liLogowanie');
        logout.innerHTML = '<a href="<?= $router->generatePath('logout-index') ?>">Wyloguj</a>';
        console.log(login);
        document.getElementById('liUser').style.visibility = 'visible';
        let pizda = document.getElementById('liUser').children;
        pizda[0].innerHTML = login+' |';
    }else{
        let logout = document.getElementById('liLogowanie');
        logout.innerHTML = '<a href="<?= $router->generatePath('login-index') ?>">Logowanie</a>';
    }
    function si(){
        let d = document.getElementById("sear");
        if(d.innerHTML !=""){
            d.innerHTML="";
            d.style=null;
        }else {
            d.style.width="200px";
            d.style.height="75px";
            d.style.position="absolute";
            d.style.paddingLeft="5px";
            let inn = document.createElement("div");
            let pracownik = document.createElement("a");
            pracownik.innerHTML = "pracownik";
            pracownik.style.color="white";
            let pracownia = document.createElement("a");
            pracownia.innerHTML = "pracownia";
            pracownia.style.color="white";
            pracownia.style.marginLeft = "5px";
            pracownik.addEventListener("click", function () {
                inn.innerHTML = "";
                let frm = document.createElement("form");
                frm.action="";
                frm.method="POST";
                let inp = document.createElement("input");
                inp.type = "text";
                inp.name = "pracownik";
                inp.placeholder = "imie nazwisko";
                let sbmt = document.createElement("input");
                sbmt.setAttribute("type", "submit");
                sbmt.id="pracownik";
                frm.appendChild(inp);
                frm.appendChild(sbmt);
                inn.appendChild(frm);

            })
            pracownia.addEventListener("click", function () {
                inn.innerHTML = "";
                let frm = document.createElement("form");
                frm.action="";
                frm.method="POST";
                let inp = document.createElement("input");
                inp.type = "text";
                inp.name = "pracownia";
                inp.placeholder = "budynek-pokoj";
                let sbmt = document.createElement("input");
                sbmt.setAttribute("type", "submit");
                sbmt.id="pracownia";
                frm.appendChild(inp);
                frm.appendChild(sbmt);
                inn.appendChild(frm);

            })
            d.appendChild(pracownik);
            d.appendChild(pracownia);
            d.appendChild(inn);
        }
    }

</script>
<?php
