<?php
namespace App\Controller;

use App\Exception\NotFoundException;
use App\Model\Pietro;
use App\Service\Router;
use App\Service\Templating;

class PietroController
{
    public function indexAction(Templating $templating, Router $router): ?string
    {
        $Pietra = Pietro::findAll();
        $html = $templating->render('Pietro/index.html.php', [
            'Pietra' => $Pietra,
            'router' => $router,
        ]);
        return $html;
    }

    public function createAction(?array $requestPietro, Templating $templating, Router $router): ?string
    {
        if ($requestPietro) {
            $Pietro = Pietro::fromArray($requestPietro);
            // @todo missing validation
            $Pietro->save();

            $path = $router->generatePath('Pietro-index');
            $router->redirect($path);
            return null;
        } else {
            $Pietro = new Pietro();
        }

        $html = $templating->render('Pietro/create.html.php', [
            'Pietro' => $Pietro,
            'router' => $router,
        ]);
        return $html;
    }

    public function editAction(int $PietroId, ?array $requestPietro, Templating $templating, Router $router): ?string
    {
        $Pietro = Pietro::find($PietroId);
        if (! $Pietro) {
            throw new NotFoundException("Missing Pietro with id $PietroId");
        }

        if ($requestPietro) {
            $Pietro->fill($requestPietro);
            // @todo missing validation
            $Pietro->save();

            $path = $router->generatePath('Pietro-index');
            $router->redirect($path);
            return null;
        }

        $html = $templating->render('Pietro/edit.html.php', [
            'Pietro' => $Pietro,
            'router' => $router,
        ]);
        return $html;
    }

    public function showAction(int $PietroId, Templating $templating, Router $router): ?string
    {
        $Pietro = Pietro::find($PietroId);
        if (! $Pietro) {
            throw new NotFoundException("Missing Pietro with id $PietroId");
        }

        $html = $templating->render('Pietro/show.html.php', [
            'Pietro' => $Pietro,
            'router' => $router,
        ]);
        return $html;
    }

    public function deleteAction(int $PietroId, Router $router): ?string
    {
        $Pietro = Pietro::find($PietroId);
        if (! $Pietro) {
            throw new NotFoundException("Missing Pietro with id $PietroId");
        }

        $Pietro->delete();
        $path = $router->generatePath('Pietro-index');
        $router->redirect($path);
        return null;
    }
}
