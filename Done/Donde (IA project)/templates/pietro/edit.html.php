<?php

/** @var \App\Model\Pietro $Pietro */
/** @var \App\Service\Router $router */

$title = "Edit Pietro {$Pietro->getBudynekId()} ({$Pietro->getPietroId()})";
$bodyClass = "edit";

ob_start(); 
session_start();
?>
    <h1><?= $title ?></h1>
    <form action="<?= $router->generatePath('Pietro-edit') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="Pietro-edit">
        <input type="hidden" name="id" value="<?= $Pietro->getPietroId() ?>">
    </form>

    <ul class="action-list">
        <li>
            <a href="<?= $router->generatePath('Pietro-index') ?>">Back to list</a></li>
        <li>
            <form action="<?= $router->generatePath('Pietro-delete') ?>" method="post">
                <input type="submit" value="Delete" onclick="return confirm('Are you sure?')">
                <input type="hidden" name="action" value="Pietro-delete">
                <input type="hidden" name="id" value="<?= $Pietro->getPietroId() ?>">
            </form>
        </li>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
