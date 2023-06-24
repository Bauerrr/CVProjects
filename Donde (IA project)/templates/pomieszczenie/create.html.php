<?php

/** @var \App\Model\pomieszczenie $pomieszczenie */
/** @var \App\Service\Router $router */

$title = 'Create Pomieszczenie';
$bodyClass = "edit";

ob_start(); 
session_start();?>
    <h1>Create Pomieszczenie</h1>
    <form action="<?= $router->generatePath('pomieszczenie-create') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="pomieszczenie-create">
    </form>

    <a href="<?= $router->generatePath('pomieszczenie-index') ?>">Back to list</a>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
