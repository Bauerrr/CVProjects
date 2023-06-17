<?php
namespace App\Model;

use App\Service\Config;

class budynek
{
    private ?int $budynek_id = null;
    private ?string $nazwa = null;
    private ?string $ulica = null;
    private ?int $nr_budynku = null;
    private ?string $kod_pocztowy = null;

    /**
     * @return int|null
     */
    public function getBudynekId(): ?int
    {
        return $this->budynek_id;
    }

    /**
     * @param int|null $budynek_id
     */
    public function setBudynekId(?int $budynek_id): void
    {
        $this->budynek_id = $budynek_id;
    }

    /**
     * @return string|null
     */
    public function getNazwa(): ?string
    {
        return $this->nazwa;
    }

    /**
     * @param string|null $nazwa
     */
    public function setNazwa(?string $nazwa): void
    {
        $this->nazwa = $nazwa;
    }

    /**
     * @return string|null
     */
    public function getUlica(): ?string
    {
        return $this->ulica;
    }

    /**
     * @param string|null $ulica
     */
    public function setUlica(?string $ulica): void
    {
        $this->ulica = $ulica;
    }

    /**
     * @return int|null
     */
    public function getNrBudynku(): ?int
    {
        return $this->nr_budynku;
    }

    /**
     * @param int|null $nr_budynku
     */
    public function setNrBudynku(?int $nr_budynku): void
    {
        $this->nr_budynku = $nr_budynku;
    }

    /**
     * @return string|null
     */
    public function getKodPocztowy(): ?string
    {
        return $this->kod_pocztowy;
    }

    /**
     * @param string|null $kod_pocztowy
     */
    public function setKodPocztowy(?string $kod_pocztowy): void
    {
        $this->kod_pocztowy = $kod_pocztowy;
    }

    /**
     * @return string|null
     */
    public function getMiasto(): ?string
    {
        return $this->miasto;
    }

    /**
     * @param string|null $miasto
     */
    public function setMiasto(?string $miasto): void
    {
        $this->miasto = $miasto;
    }

    /**
     * @return string|null
     */
    public function getKraj(): ?string
    {
        return $this->kraj;
    }

    /**
     * @param string|null $kraj
     */
    public function setKraj(?string $kraj): void
    {
        $this->kraj = $kraj;
    }
    private ?string $miasto = null;
    private ?string $kraj = null;


    public static function fromArray($array): budynek
    {
        $post = new self();
        $post->fill($array);

        return $post;
    }

    public function fill($array): budynek
    {
        if (isset($array['budynek_id']) && ! $this->getBudynekId()) {
            $this->setBudynekId($array['budynek_id']);
        }
        if (isset($array['kod_pocztowy'])){
            $this->setKodPocztowy($array['kod_pocztowy']);
        }
        if (isset($array['kraj'])){
            $this->setKraj($array['kraj']);
        }
        if (isset($array['miasto'])){
            $this->setMiasto($array['miasto']);
        }
        if (isset($array['nazwa'])){
            $this->setNazwa($array['nazwa']);
        }
        if (isset($array['nr_budynku'])){
            $this->setNrBudynku($array['nr_budynku']);
        }
        if (isset($array['ulica'])){
            $this->setUlica($array['ulica']);
        }
        return $this;
    }

    public static function findAll(): array
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM budynek';
        $statement = $pdo->prepare($sql);
        $statement->execute();

        $budynki = [];
        $budynkiArray = $statement->fetchAll(\PDO::FETCH_ASSOC);
        foreach ($budynkiArray as $budynekArray) {
            $budynki[] = self::fromArray($budynekArray);
        }

        return $budynki;
    }

    public static function find($id): ?budynek
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM budynek WHERE budynek_id = :id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['id' => $id]);

        $budynekArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $budynekArray) {
            return null;
        }
        $budynek = budynek::fromArray($budynekArray);

        return $budynek;
    }

    public function save(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        if (! $this->getBudynekId()) {
            $sql = "INSERT INTO budynek (nazwa, ulica, nr_budynku, kod_pocztowy, miasto, kraj) VALUES (:nazwa, :ulica, :nr_budynku,
            :kod_pocztowy, :miasto, :kraj)";

            $statement = $pdo->prepare($sql);
            $statement->execute([
                'nazwa' => $this->getNazwa(),
                'ulica' => $this->getUlica(),
                'nr_budynku' => $this->getNrBudynku(),
                'kod_pocztowy' => $this->getKodPocztowy(),
                'miasto' => $this->getMiasto(),
                'kraj' => $this->getKraj(),
            ]);

            $this->setBudynekId($pdo->lastInsertId());
        } else {
            $sql = "UPDATE budynek SET nazwa = :nazwa, ulica = :ulica, nr_budynku = :nr_budynku, kod_pocztowy = :kod_pocztowy, 
            miasto = :miasto, kraj = :kraj WHERE budynek_id = :id";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                ':nazwa' => $this->getNazwa(),
                ':ulica' => $this->getUlica(),
                ':nr_budynku' => $this->getNrBudynku(),
                ':kod_pocztowy' => $this->getKodPocztowy(),
                ':miasto' => $this->getMiasto(),
                ':kraj' => $this->getKraj(),
                ':id' => $this->getBudynekId(),
            ]);
        }
    }

    public function delete(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));

        $sql5= "SELECT pietro_id from pietro where budynek_id = :budynek_id";
        $statement = $pdo->prepare($sql5);
        $statement->execute(['budynek_id' => $this->getBudynekId()]);
        while($data2 = $statement->fetch(\PDO::FETCH_ASSOC)) {
            $sql4 = "SELECT pomieszczenie_id from pomieszczenie where pietro_id = :pietro_id";
            $statement3 = $pdo->prepare($sql4);
            $statement3->execute(['pietro_id' => $data2['pietro_id']]);

            //$myfile = fopen("output.txt", "a") or die("Unable to open file!");
            while ($data = $statement3->fetch(\PDO::FETCH_ASSOC)) {

                $sql2 = "DELETE FROM pracownik_pomieszczenie WHERE pomieszczenie_id = :pomieszczenie_id";
                $statement2 = $pdo->prepare($sql2);
                $statement2->execute([
                    ':pomieszczenie_id' => $data['pomieszczenie_id'],
                ]);

                $sql3 = "DELETE FROM pomieszczenie WHERE pomieszczenie_id = :pomieszczenie_id";
                $statement2 = $pdo->prepare($sql3);
                $statement2->execute([
                    ':pomieszczenie_id' => $data['pomieszczenie_id'],
                ]);

                // fwrite($myfile, $data['pomieszczenie_id'] . PHP_EOL);
            }

            $sql = "DELETE FROM pietro WHERE pietro_id = :pietro_id";
            $statement4 = $pdo->prepare($sql);
            $statement4->execute([
                ':pietro_id' => $data2['pietro_id'],
            ]);
        }

        $sql = "DELETE FROM budynek WHERE budynek_id = :id";
        $statement = $pdo->prepare($sql);
        $statement->execute([
            ':id' => $this->getBudynekId(),
        ]);

        $this->setBudynekId(null);
        $this->setUlica(null);
        $this->setNrBudynku(null);
        $this->setNazwa(null);
        $this->setKodPocztowy(null);
        $this->setKraj(null);
        $this->setMiasto(null);
    }
}
