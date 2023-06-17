<?php
namespace App\Controller;

use App\Exception\NotFoundException;
use App\Model\pomieszczenie;
use App\Service\Router;
use App\Service\Templating;

class pomieszczenieController
{
    public function indexAction(Templating $templating, Router $router): ?string
    {
        $pomieszczenia = pomieszczenie::findAll();
        $html = $templating->render('pomieszczenie/index.html.php', [
            'pomieszczenia' => $pomieszczenia,
            'router' => $router,
        ]);
        return $html;
    }

    public function createAction(?array $requestPomieszczenie, Templating $templating, Router $router): ?string
    {
        if ($requestPomieszczenie) {
            $pomieszczenie = pomieszczenie::fromArray($requestPomieszczenie);
            // @todo missing validation
            $pomieszczenie->save();

            $path = $router->generatePath('pomieszczenie-index');
            $router->redirect($path);
            return null;
        } else {
            $pomieszczenie = new pomieszczenie();
        }

        $html = $templating->render('pomieszczenie/create.html.php', [
            'pomieszczenie' => $pomieszczenie,
            'router' => $router,
        ]);
        return $html;
    }

    public function editAction(int $pomieszczenieId, ?array $requestPomieszczenie, Templating $templating, Router $router): ?string
    {
        $pomieszczenie = pomieszczenie::find($pomieszczenieId);
        if (! $pomieszczenie) {
            throw new NotFoundException("Missing pomieszczenie with id $pomieszczenieId");
        }

        if ($requestPomieszczenie) {
            $pomieszczenie->fill($requestPomieszczenie);
            // @todo missing validation
            $pomieszczenie->save();

            $path = $router->generatePath('pomieszczenie-index');
            $router->redirect($path);
            return null;
        }

        $html = $templating->render('pomieszczenie/edit.html.php', [
            'pomieszczenie' => $pomieszczenie,
            'router' => $router,
        ]);
        return $html;
    }

    public function showAction(int $pomieszczenieId, Templating $templating, Router $router): ?string
    {
        $pomieszczenie = pomieszczenie::find($pomieszczenieId);
        if (! $pomieszczenie) {
            throw new NotFoundException("Missing pomieszczenie with id $pomieszczenieId");
        }

        $html = $templating->render('pomieszczenie/show.html.php', [
            'pomieszczenie' => $pomieszczenie,
            'router' => $router,
        ]);
        return $html;
    }

    public function deleteAction(int $pomieszczenieId, Router $router): ?string
    {
        $pomieszczenie = pomieszczenie::find($pomieszczenieId);
        if (! $pomieszczenie) {
            throw new NotFoundException("Missing pomieszczenie with id $pomieszczenieId");
        }

        $pomieszczenie->delete();
        $path = $router->generatePath('pomieszczenie-index');
        $router->redirect($path);
        return null;
    }
}
