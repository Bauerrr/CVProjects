<?php
namespace App\Model;

use App\Service\Config;

class pomieszczenie
{
    private ?int $pomieszczenie_id = null;
    private ?string $numer = null;
    private ?int $pietro_id = null;

    public function getPomieszczenie_id(): ?int
    {
        return $this->pomieszczenie_id;
    }

    public function setPomieszczenie_id(?int $pomieszczenie_id): pomieszczenie
    {
        $this->pomieszczenie_id = $pomieszczenie_id;

        return $this;
    }

    public function getNumer(): ?string
    {
        return $this->numer;
    }

    public function setNumer(?string $numer): pomieszczenie
    {
        $this->numer = $numer;

        return $this;
    }

    public function getPietro_id(): ?int
    {
        return $this->pietro_id;
    }

    public function setPietro_id(?int $pietro_id): pomieszczenie
    {
        $this->pietro_id = $pietro_id;

        return $this;
    }

    public static function fromArray($array): pomieszczenie
    {
        $pomieszczenie = new self();
        $pomieszczenie->fill($array);

        return $pomieszczenie;
    }

    public function fill($array): pomieszczenie
    {
        if (isset($array['pomieszczenie_id']) && ! $this->getPomieszczenie_id()) {
            $this->setPomieszczenie_id($array['pomieszczenie_id']);
        }
        if (isset($array['numer'])) {
            $this->setNumer($array['numer']);
        }
        if (isset($array['pietro_id'])) {
            $this->setPietro_id($array['pietro_id']);
        }

        return $this;
    }

    public static function findAll(): array
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie';
        $statement = $pdo->prepare($sql);
        $statement->execute();

        $pomieszczenia = [];
        $pomieszczeniaArray = $statement->fetchAll(\PDO::FETCH_ASSOC);
        foreach ($pomieszczeniaArray as $pomieszczenieArray) {
            $pomieszczenia[] = self::fromArray($pomieszczenieArray);
        }

        return $pomieszczenia;
    }

    public static function find($pomieszczenie_id): ?pomieszczenie
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie WHERE pomieszczenie_id = :pomieszczenie_id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['pomieszczenie_id' => $pomieszczenie_id]);

        $pomieszczenieArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $pomieszczenieArray) {
            return null;
        }
        $pomieszczenie = pomieszczenie::fromArray($pomieszczenieArray);

        return $pomieszczenie;
    }

    public static function findpom($nr_pomieszczenia): ?pomieszczenie
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie WHERE numer = :nr_pomieszczenia';
        $statement = $pdo->prepare($sql);
        $statement->execute(['nr_pomieszczenia' => $nr_pomieszczenia]);

        $pomieszczenieArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $pomieszczenieArray) {
            return null;
        }
        $pomieszczenie = pomieszczenie::fromArray($pomieszczenieArray);

        return $pomieszczenie;
    }
<<<<<<< HEAD
    
=======

>>>>>>> 90b121171c2d086ccc6966ccbe003e2fc6f45533
    public static function findPomPietro($nr_pomieszczenia, $pietro_id): ?pomieszczenie
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pomieszczenie WHERE numer = :nr_pomieszczenia AND pietro_id = :pietro_id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['nr_pomieszczenia' => $nr_pomieszczenia, 'pietro_id' => $pietro_id]);

        $pomieszczenieArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $pomieszczenieArray) {
            return null;
        }
        $pomieszczenie = pomieszczenie::fromArray($pomieszczenieArray);

        return $pomieszczenie;
    }

    public function save(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        if (! $this->getPomieszczenie_id()) {
            $sql = "INSERT INTO pomieszczenie (numer, pietro_id) VALUES (:numer, :pietro_id)";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                'numer' => $this->getNumer(),
                'pietro_id' => $this->getPietro_id(),
            ]);

            $this->setPomieszczenie_id($pdo->lastInsertId());
        } else {
            $sql = "UPDATE pomieszczenie SET numer = :numer, pietro_id = :pietro_id WHERE pomieszczenie_id = :pomieszczenie_id";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                ':numer' => $this->getNumer(),
                ':pietro_id' => $this->getPietro_id(),
                ':pomieszczenie_id' => $this->getPomieszczenie_id(),
            ]);
        }
    }

    public function delete(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));

        $sql2 = "DELETE FROM pracownik_pomieszczenie WHERE pomieszczenie_id = :pomieszczenie_id";
        $statement = $pdo->prepare($sql2);
        $statement->execute([
            ':pomieszczenie_id' => $this->getPomieszczenie_id(),
        ]);


        $sql = "DELETE FROM pomieszczenie WHERE pomieszczenie_id = :pomieszczenie_id";
        $statement = $pdo->prepare($sql);
        $statement->execute([
            ':pomieszczenie_id' => $this->getPomieszczenie_id(),
        ]);

        $this->setPomieszczenie_id(null);
        $this->setNumer(null);
        $this->setPietro_id(null);
    }
}
