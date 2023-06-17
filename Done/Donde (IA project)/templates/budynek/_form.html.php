<?php
    /** @var $post ?\App\Model\budynek */
?>

<div class="form-group">
    <label for="nazwa">nazwa</label>
    <input type="text" id="nazwa" name="budynek[nazwa]" value="<?= $post ? $post->getNazwa() : '' ?>">
</div>
<div class="form-group">
    <label for="kraj">kraj</label>
    <input type="text" id="kraj" name="budynek[kraj]" value="<?= $post ? $post->getKraj() : '' ?>">
</div>

<div class="form-group">
    <label for="miasto">miasto</label>
    <input type="text" id="miasto" name="budynek[miasto]" value="<?= $post ? $post->getMiasto() : '' ?>">
</div>

<div class="form-group">
    <label for="kod_pocztowy">kod pocztowy</label>
    <input type="text" id="kod_pocztowy" name="budynek[kod_pocztowy]" value="<?= $post ? $post->getKodPocztowy() : '' ?>">
</div>

<div class="form-group">
    <label for="ulica">ulica</label>
    <input type="text" id="ulica" name="budynek[ulica]" value="<?= $post ? $post->getUlica() : '' ?>">
</div>

<div class="form-group">
    <label for="nr_budynku">nr budynku</label>
    <input type="text" id="nr_budynku" name="budynek[nr_budynku]" value="<?= $post ? $post->getNrBudynku(): '' ?>">
</div>

<div class="form-group">
    <label></label>
    <input type="submit" value="Submit">
</div>
