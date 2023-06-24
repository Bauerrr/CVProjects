<?php

/** @var \App\Model\pracownik[] $posts */
/** @var \App\Service\Router $router */
use App\Model\pracownik;

$title = 'Pracownik List';
$bodyClass = 'index';

ob_start(); 
session_start();
?>
    <div class = "nawigacja">
        <h2>Panel Administratora</h2>
        <ul>
            
            <li><a href="<?= $router->generatePath('pracownik-index');?>" style="color: #006AFF">Pracownicy</a></li>

            <li><a href="<?= $router->generatePath('pomieszczenie-index');?>">Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('pracownik_pomieszczenie-index');?>">Pracownicy-Pomieszczenia</a></li>

            <li><a href="<?= $router->generatePath('Pietro-index');?>">Piętra</a></li>
        </ul>
    </div>
    <div class = "import">
        <p id="importP">Import pracowników z pliku CSV</p>
        <form method="post" enctype="multipart/form-data">
            <label for="file-upload" id="label-for-file-upload">
                Wybierz plik
                <input name="plik" type="file" value="Wybierz plik" id="file-upload"></input>
            </label>
            <input type="submit" value="Importuj"></input>
        </form>
    </div>
    
    <a id="dodajPrac" href="<?= $router->generatePath('pracownik-create') ?>">Dodaj pracownika</a>

    <ul class="index-list">
        <?php foreach ($posts as $post): ?>
            <li><p><?= $post->getTytul()  ?> <?= $post->getImie()  ?> <?= $post->getNazwisko()  ?></p>
                <ul class="action-list">
                    <li><a href="<?= $router->generatePath('pracownik-show', ['id' => $post->getPracownikId()]) ?>">Details</a></li>
                    <li><a href="<?= $router->generatePath('pracownik-edit', ['id' => $post->getPracownikId()]) ?>">Edit</a></li>
                </ul>
            </li>
        <?php endforeach; ?>
    </ul>

    <?php 
    if(isset($_FILES["plik"])){
        $target_file = $_FILES["plik"]["tmp_name"];
        // foreach($target_file as $line){
        //     echo $line;
        // }
        $my_file = fopen($target_file, "r") or die("Unable to open file!");
        if($my_file){
            Pracownik::purge();
            while(($line=fgetcsv($my_file)) !== false){
                $array = [
                    "imie" => $line[0],
                    "nazwisko" => $line[1],
                    "tytul" => $line[2],
                    "gabinet" => $line[3]
                ];
                $newPracownik = Pracownik::fromArray($array);
                $newPracownik->save();
            }
            fclose($my_file);
            header("Refresh:0");
        }
        
    }
    ?>
    <script>
        let fileName = document.getElementById("importP")
        document.getElementById("file-upload").addEventListener("change", ()=>{
            let inputFile = document.getElementById("file-upload").files[0];
            console.log(inputFile.name);
            fileName.innerText = "Import pracowników z pliku CSV: " + inputFile.name;
        })
    </script>
<?php $main = ob_get_clean();

include __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'base.html.php';
