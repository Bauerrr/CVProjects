
<?php
/** @var \App\Service\Router $router */
/** @var \App\Model\uzytkownik $ */
use App\Model\uzytkownik;

$templating = new \App\Service\Templating();
$title = 'Main strona';
$bodyClass = 'index';
$router = new \App\Service\Router();



ob_start();

session_start();

    if (isset($_POST['login']) && isset($_POST['haslo'])){
        // $login = $_POST['login'];
        // $haslo = $_POST['haslo'];
        // if ($login == "admin" && $haslo == "Admin1!"){
        //     header("Location: twojastara.php?");
        // } else
        //     echo '<script>alert("Błędny login/hasło!")</script>';
        function validate($data){

            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
     
            return $data;
        }
        $login = $_POST['login'];
        $haslo = $_POST['haslo'];
       

        if(empty($login)){
            header("Location: index.php?error= Wymagana nazwa uzytkownika");
            exit();
        } else if(empty($haslo)){
            header("Location: index.php?error= Wymagane haslo");
            exit();
        }else{
            
            $user = uzytkownik::find_id(1);
            //echo $user->getLog();
            //echo $user->getHaslo();
            //echo $login;
            //echo $haslo;
            if($user!=null){
                
                if($user->getLog() == $login && $user->getHaslo() == $haslo){
                    //echo "Zalogowano";
                    $_SESSION['login'] = $user->getLog();
                    $path = $router->generatePath('');
                    $router->redirect($path);
                    //echo 'dobrze';
                    //exit();
                    
                }else{
                    //header("Location: index.php?error=Nieprawidlowy login lub haslo");
                    echo 'zle';
                    exit();
                }
            }
        }

    }

$main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
?>
