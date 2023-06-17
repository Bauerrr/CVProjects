<?php
require_once __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'autoload.php';

$config = new \App\Service\Config();

$templating = new \App\Service\Templating();
$router = new \App\Service\Router();

$action = $_REQUEST['action'] ?? null;
switch ($action) {
    case 'base':
    case null:
        $view = $templating->render('glowna/index.html.php', [
            'router' => $router,]);
        break;
    case 'mapa':
        $view = $templating->render('glowna/index.html.php', [
            'router' => $router,]);
        break;
    case 'login-index':
        $view = $templating->render('glowna/login.php', [
            'router' => $router,
        ]);
        break;
    case 'login-kurwa':
        $view = $templating->render('glowna/login_script.php', [
            'router' => $router,
        ]);
        break;
    case 'logout-index':
        $view = $templating->render('glowna/logout.php', [
            'router' => $router,]);
        break;
    case 'admin-index':
        $view = $templating->render('glowna/admin.php', [
            'router' => $router,]);
        break;
    case 'pracownik-index':
        $controller = new \App\Controller\pracownikController();
        $view = $controller->indexAction($templating, $router);
        break;
    case 'pracownik-create':
        $controller = new \App\Controller\pracownikController();
        $view = $controller->createAction($_REQUEST['pracownik'] ?? null, $templating, $router);
        break;
    case 'pracownik-edit':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pracownikController();
        $view = $controller->editAction($_REQUEST['id'], $_REQUEST['pracownik'] ?? null, $templating, $router);
        break;
    case 'pracownik-show':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pracownikController();
        $view = $controller->showAction($_REQUEST['id'], $templating, $router);
        break;
    case 'pracownik-delete':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pracownikController();
        $view = $controller->deleteAction($_REQUEST['id'], $router);
        break;
    case 'pomieszczenie-index':
        $controller = new \App\Controller\pomieszczenieController();
        $view = $controller->indexAction($templating, $router);
        break;
    case 'pomieszczenie-create':
        $controller = new \App\Controller\pomieszczenieController();
        $view = $controller->createAction($_REQUEST['pomieszczenie'] ?? null, $templating, $router);
        break;
    case 'pomieszczenie-edit':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pomieszczenieController();
        $view = $controller->editAction($_REQUEST['id'], $_REQUEST['pomieszczenie'] ?? null, $templating, $router);
        break;
    case 'pomieszczenie-show':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pomieszczenieController();
        $view = $controller->showAction($_REQUEST['id'], $templating, $router);
        break;
    case 'pomieszczenie-delete':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pomieszczenieController();
        $view = $controller->deleteAction($_REQUEST['id'], $router);
        break;    
    case 'Pietro-index':
        $controller = new \App\Controller\PietroController();
        $view = $controller->indexAction($templating, $router);
        break;
    case 'Pietro-create':
        $controller = new \App\Controller\PietroController();
        $view = $controller->createAction($_REQUEST['Pietro'] ?? null, $templating, $router);
        break;
    case 'Pietro-edit':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\PietroController();
        $view = $controller->editAction($_REQUEST['id'], $_REQUEST['Pietro'] ?? null, $templating, $router);
        break;
    case 'Pietro-show':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\PietroController();
        $view = $controller->showAction($_REQUEST['id'], $templating, $router);
        break;
    case 'Pietro-delete':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\PietroController();
        $view = $controller->deleteAction($_REQUEST['id'], $router);
        break;
    case 'pracownik_pomieszczenie-index':
        $controller = new \App\Controller\pracownik_pomieszczenieController();
        $view = $controller->indexAction($templating, $router);
        break;
    case 'pracownik_pomieszczenie-create':
        $controller = new \App\Controller\pracownik_pomieszczenieController();
        $view = $controller->createActionAll($_REQUEST['pracownik'] ?? null, $_REQUEST['Pietro'] ?? null, $_REQUEST['pomieszczenie'] ?? null, $templating, $router);
        break;
    case 'pracownik_pomieszczenie-edit':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pracownik_pomieszczenieController();
        $view = $controller->editAction($_REQUEST['id'], $_REQUEST['pracownik_pomieszczenie'] ?? null, $templating, $router);
        break;
    case 'pracownik_pomieszczenie-show':
        if (! $_REQUEST['id']) {
            break;
        }
        $controller = new \App\Controller\pracownik_pomieszczenieController();
        $view = $controller->showAction($_REQUEST['id'], $templating, $router);
        break;
    case 'pracownik_pomieszczenie-delete':
        if (! $_REQUEST['id']) {
            break;
        }
    default:
        $myfile = fopen("output.txt", "w") or die("Unable to open file!");
        fwrite($myfile, 'nie dziala');

    

}
// $action = $_REQUEST['action'] ?? null;
// switch ($action) {
//    case 'pomieszczenie-index':
//    case null:
//        $controller = new \App\Controller\pomieszczenieController();
//        $view = $controller->indexAction($templating, $router);
//        break;
//    case 'pomieszczenie-create':
//        $controller = new \App\Controller\pomieszczenieController();
//        $view = $controller->createAction($_REQUEST['pomieszczenie'] ?? null, $templating, $router);
//        break;
//    case 'pomieszczenie-edit':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\pomieszczenieController();
//        $view = $controller->editAction($_REQUEST['id'], $_REQUEST['pomieszczenie'] ?? null, $templating, $router);
//        break;
//    case 'pomieszczenie-show':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\pomieszczenieController();
//        $view = $controller->showAction($_REQUEST['id'], $templating, $router);
//        break;
//    case 'pomieszczenie-delete':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\pomieszczenieController();
//    case 'Pietro-index':
//        case null:
//            $controller = new \App\Controller\PietroController();
//            $view = $controller->indexAction($templating, $router);
//            break;
//        case 'Pietro-create':
//            $controller = new \App\Controller\PietroController();
//            $view = $controller->createAction($_REQUEST['Pietro'] ?? null, $templating, $router);
//            break;
//        case 'Pietro-edit':
//            if (! $_REQUEST['id']) {
//                break;
//            }
//            $controller = new \App\Controller\PietroController();
//            $view = $controller->editAction($_REQUEST['id'], $_REQUEST['Pietro'] ?? null, $templating, $router);
//            break;
//        case 'Pietro-show':
//            if (! $_REQUEST['id']) {
//                break;
//            }
//            $controller = new \App\Controller\PietroController();
//            $view = $controller->showAction($_REQUEST['id'], $templating, $router);
//            break;
//        case 'Pietro-delete':
//            if (! $_REQUEST['id']) {
//                break;
//            }
//            $controller = new \App\Controller\PietroController();
//            $view = $controller->deleteAction($_REQUEST['id'], $router);
//            break;
//        default:
//            $view = 'Not found';
//            break;
//    case 'pracownik-index':
//    case null:
//        $controller = new \App\Controller\pracownikController();
//        $view = $controller->indexAction($templating, $router);
//        break;
//    case 'pracownik-create':
//        $controller = new \App\Controller\pracownikController();
//        $view = $controller->createAction($_REQUEST['pracownik'] ?? null, $templating, $router);
//        break;
//    case 'pracownik-edit':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\pracownikController();
//        $view = $controller->editAction($_REQUEST['id'], $_REQUEST['pracownik'] ?? null, $templating, $router);
//        break;
//    case 'pracownik-show':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\pracownikController();
//        $view = $controller->showAction($_REQUEST['id'], $templating, $router);
//        break;
//    case 'pracownik-delete':
//        if (! $_REQUEST['id']) {
//            break;
//        }
//        $controller = new \App\Controller\pracownikController();
//        $view = $controller->deleteAction($_REQUEST['id'], $router);
//        break;
//    default:
//        $view = 'Not found';
//        break;
    // case 'budynek-index':
    // case null:
    //     $controller = new \App\Controller\budynekController();
    //     $view = $controller->indexAction($templating, $router);
    //     break;
    // case 'budynek-create':
    //     $controller = new \App\Controller\budynekController();
    //     $view = $controller->createAction($_REQUEST['budynek'] ?? null, $templating, $router);
    //     break;
    // case 'budynek-edit':
    //     if (! $_REQUEST['id']) {
    //         break;
    //     }
    //     $controller = new \App\Controller\budynekController();
    //     $view = $controller->editAction($_REQUEST['id'], $_REQUEST['budynek'] ?? null, $templating, $router);
    //     break;
    // case 'budynek-show':
    //     if (! $_REQUEST['id']) {
    //         break;
    //     }
    //     $controller = new \App\Controller\budynekController();
    //     $view = $controller->showAction($_REQUEST['id'], $templating, $router);
    //     break;
    // case 'budynek-delete':
    //     if (! $_REQUEST['id']) {
    //         break;
    //     }
    //     $controller = new \App\Controller\budynekController();
    //     $view = $controller->deleteAction($_REQUEST['id'], $router);
    //     break;
    // default:
    //     $view = 'Not found';
    //     break;


// }

if ($view) {
    echo $view;
}
