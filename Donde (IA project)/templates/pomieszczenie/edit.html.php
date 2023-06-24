<?php

/** @var \App\Model\pomieszczenie $pomieszczenie */
/** @var \App\Service\Router $router */

$title = "Edit pomieszczenie {$pomieszczenie->getNumer()} ({$pomieszczenie->getPomieszczenie_id()})";
$bodyClass = "edit";

ob_start(); 
session_start();
?>
    <h1><?= $title ?></h1>
    <form action="<?= $router->generatePath('pomieszczenie-edit') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="pomieszczenie-edit">
        <input type="hidden" name="id" value="<?= $pomieszczenie->getPomieszczenie_id() ?>">
    </form>

    <ul class="action-list">
        <li>
            <a href="<?= $router->generatePath('pomieszczenie-index') ?>">Back to list</a></li>
        <li>
            <form action="<?= $router->generatePath('pomieszczenie-delete') ?>" method="post">
                <input type="submit" value="Delete" onclick="return confirm('Are you sure?')">
                <input type="hidden" name="action" value="pomieszczenie-delete">
                <input type="hidden" name="id" value="<?= $pomieszczenie->getPomieszczenie_id() ?>">
            </form>
        </li>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
