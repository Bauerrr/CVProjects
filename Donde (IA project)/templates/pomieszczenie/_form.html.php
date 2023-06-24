<?php
    /** @var $pomieszczenie ?\App\Model\pomieszczenie */
?>

<div class="form-group">
    <label for="numer">Numer</label>
    <input type="text" id="numer" name="pomieszczenie[numer]" value="<?= $pomieszczenie ? $pomieszczenie->getNumer() : '' ?>">
</div>

<div class="form-group">
    <label for="pietro_id">Pietro_id</label>
    <textarea id="pietro_id" name="pomieszczenie[pietro_id]"><?= $pomieszczenie? $pomieszczenie->getPietro_id() : '' ?></textarea>
</div>

<div class="form-group">
    <label></label>
    <input type="submit" value="Submit">
</div>
