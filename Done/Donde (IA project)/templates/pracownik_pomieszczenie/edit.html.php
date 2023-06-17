<?php

/** @var \App\Model\pracownik_pomieszczenie $pracownik_pomieszczenie */
/** @var \App\Service\Router $router */

// $title = "Edit Pracownik-Pomieszczenie {$postman->getTytul()} {$postman->getImie()} {$postman->getNazwisko()} ";
$title = "Edit Pracownik-Pomieszczenie";
$bodyClass = "edit";

ob_start();
session_start();?>
    <h1><?= $title ?></h1>
    <form action="<?= $router->generatePath('pracownik_pomieszczenie-edit') ?>" method="post" class="edit-form">
        <?php require __DIR__ . DIRECTORY_SEPARATOR . '_form.html.php'; ?>
        <input type="hidden" name="action" value="pracownik_pomieszczenie-edit">
        <input type="hidden" name="id" value="<?= $pracownik_pomieszczenie->getPracownik_pomieszczenie_id() ?>">
    </form>

    <ul class="action-list">
        <li>
            <a href="<?= $router->generatePath('pracownik_pomieszczenie-index') ?>">Back to list</a></li>
        <li>
            <form action="<?= $router->generatePath('pracownik_pomieszczenie-delete') ?>" method="post">
                <input type="submit" value="Delete" onclick="return confirm('Are you sure?')">
                <input type="hidden" name="action" value="pracownik_pomieszczenie-delete">
                <input type="hidden" name="id" value="<?= $pracownik_pomieszczenie->getPracownik_pomieszczenie_id() ?>">
            </form>
        </li>
    </ul>

<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
