<?php

/** @var \App\Model\pracownik $post */
/** @var \App\Service\Router $router */

$title = "Edit Pracownik {$post->getTytul()} {$post->getImie()} {$post->getNazwisko()} ";
$bodyClass = "edit";

ob_start();
session_start();?>
    <h1><?= $title ?></h1>
    <form action="<?= $router->generatePath('pracownik-edit') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="pracownik-edit">
        <input type="hidden" name="id" value="<?= $post->getPracownikId() ?>">
    </form>

    <ul class="action-list">
        <li>
            <a href="<?= $router->generatePath('pracownik-index') ?>">Back to list</a></li>
        <li>
            <form action="<?= $router->generatePath('pracownik-delete') ?>" method="post">
                <input type="submit" value="Delete" onclick="return confirm('Are you sure?')">
                <input type="hidden" name="action" value="pracownik-delete">
                <input type="hidden" name="id" value="<?= $post->getPracownikId() ?>">
            </form>
        </li>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
