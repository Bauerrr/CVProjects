<?php

/** @var \App\Model\budynek $post */
/** @var \App\Service\Router $router */

$title = "Edit budynek {$post->getNazwa()} ({$post->getBudynekId()})";
$bodyClass = "edit";

ob_start(); ?>
    <h1><?= $title ?></h1>
    <form action="<?= $router->generatePath('budynek-edit') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="budynek-edit">
        <input type="hidden" name="id" value="<?= $post->getBudynekId() ?>">
    </form>

    <ul class="action-list">
        <li>
            <a href="<?= $router->generatePath('budynek-index') ?>">Back to list</a></li>
        <li>
            <form action="<?= $router->generatePath('budynek-delete') ?>" method="post">
                <input type="submit" value="Delete" onclick="return confirm('Are you sure?')">
                <input type="hidden" name="action" value="budynek-delete">
                <input type="hidden" name="id" value="<?= $post->getBudynekId() ?>">
            </form>
        </li>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
