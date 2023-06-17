<?php
session_start();
session_unset();
session_destroy();

$path = $router->generatePath('');
$router->redirect($path);