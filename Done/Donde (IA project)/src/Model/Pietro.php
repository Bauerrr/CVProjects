<?php
namespace App\Model;

use App\Service\Config;

class Pietro
{
    private ?int $pietro_id = null;
    private ?int $budynek_id = null;
    private ?string $nazwa = null;

    /**
     * @return int|null
     */
    public function getPietroId(): ?int
    {
        return $this->pietro_id;
    }

    /**
     * @param int|null $pietro_id
     */
    public function setPietroId(?int $pietro_id): void
    {
        $this->pietro_id = $pietro_id;
    }

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


    public static function fromArray($array): Pietro
    {
        $pietro = new self();
        $pietro->fill($array);

        return $pietro;
    }

    public function fill($array): Pietro
    {
        if (isset($array['pietro_id']) && ! $this->getPietroId()) {
            $this->setPietroId($array['pietro_id']);
        }
        if (isset($array['budynek_id'])) {
            $this->setBudynekId($array['budynek_id']);
        }
        if (isset($array['nazwa'])) {
            $this->setNazwa($array['nazwa']);
        }

        return $this;
    }

    public static function findAll(): array
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pietro';
        $statement = $pdo->prepare($sql);
        $statement->execute();

        $pietra = [];
        $pietraArray = $statement->fetchAll(\PDO::FETCH_ASSOC);
        foreach ($pietraArray as $pietroArray) {
            $pietra[] = self::fromArray($pietroArray);
        }

        return $pietra;
    }

    public static function find($pietro_id): ?Pietro
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pietro WHERE pietro_id = :pietro_id';
        $statement = $pdo->prepare($sql);
        $statement->execute(['pietro_id' => $pietro_id]);

        $pietroArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $pietroArray) {
            return null;
        }
        $pietro = Pietro::fromArray($pietroArray);

        return $pietro;
    }

    public static function findName($pietro_name): ?Pietro
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        $sql = 'SELECT * FROM pietro WHERE nazwa = :pietro_name';
        $statement = $pdo->prepare($sql);
        $statement->execute(['nazwa' => $pietro_name]);

        $pietroArray = $statement->fetch(\PDO::FETCH_ASSOC);
        if (! $pietroArray) {
            return null;
        }
        $pietro = Pietro::fromArray($pietroArray);

        return $pietro;
    }

    public function save(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));
        if (! $this->getPietroId()) {
            $sql = "INSERT INTO pietro (budynek_id, nazwa) VALUES (:budynek_id, :nazwa)";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                'budynek_id' => $this->getBudynekId(),
                'nazwa' => $this->getNazwa(),
            ]);

            $this->setPietroId($pdo->lastInsertId());
        } else {
            $sql = "UPDATE pietro SET budynek_id = :budynek_id, nazwa = :nazwa WHERE pietro_id = :pietro_id";
            $statement = $pdo->prepare($sql);
            $statement->execute([
                ':budynek_id' => $this->getBudynekId(),
                ':nazwa' => $this->getNazwa(),
                ':pietro_id' => $this->getPietroId(),
            ]);
        }
    }

    public function delete(): void
    {
        $pdo = new \PDO(Config::get('db_dsn'), Config::get('db_user'), Config::get('db_pass'));

        $sql4 = "SELECT pomieszczenie_id from pomieszczenie where pietro_id = :pietro_id";
        $statement = $pdo->prepare($sql4);
        $statement->execute(['pietro_id' => $this->getPietroId()]);

        //$myfile = fopen("output.txt", "a") or die("Unable to open file!");
        while($data = $statement->fetch(\PDO::FETCH_ASSOC)){
            
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
        $statement = $pdo->prepare($sql);
        $statement->execute([
            ':pietro_id' => $this->getPietroId(),
        ]);

        $this->setPietroId(null);
        $this->setBudynekId(null);
        $this->setNazwa(null);
    }
}