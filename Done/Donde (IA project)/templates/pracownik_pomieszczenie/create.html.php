<?php

/** @var \App\Model\pracownik_pomieszczenie $pracownik_pomieszczenie */
/** @var \App\Service\Router $router */

$title = 'Create Pracownik-Pomieszczenie';
$bodyClass = "edit";

ob_start(); 
session_start();?>
    <h1>Create Pracownik-Pomieszczenie</h1>
    <form action="<?= $router->generatePath('pracownik_pomieszczenie-create') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="pracownik_pomieszczenie-create">
    </form>

    <a href="<?= $router->generatePath('pracownik_pomieszczenie-index') ?>">Back to list</a>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
