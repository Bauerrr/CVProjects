<?php

/** @var \App\Model\pracownik $post */
/** @var \App\Service\Router $router */

$title = 'Create Pracownik';
$bodyClass = "edit";

ob_start(); 
session_start();?>
    <h1>Create Pracownik</h1>
    <form action="<?= $router->generatePath('pracownik-create') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="pracownik-create">
    </form>

    <a href="<?= $router->generatePath('pracownik-index') ?>">Back to list</a>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
