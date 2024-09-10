<?php

$errorMessages = [];
$regexName = '/^[a-zA-ZéèàêâùïüëçæœÉÈÇÙÆŒ-]+$/';
$regexTextArea = '/^[a-zA-Z0-9éèàêâùïüëçæœÉÈÇÙÆŒ .;:,_!?()=*&\"\'$€~-]+$/';


if (isset($_POST['submit'])) {

    if (isset($_POST['lastname'])) {
        if (!preg_match($regexName, $_POST['lastname'])) {
            $errorMessages['lastname'] = 'Veuillez renseigner un nom valide.';
        }
        if (empty($_POST['lastname'])) {
            $errorMessages['lastname'] = 'Veuillez renseigner votre nom.';
        }
    }

    if (isset($_POST['firstname'])) {
        if (!preg_match($regexName, $_POST['firstname'])) {
            $errorMessages['firstname'] = 'Veuillez renseigner un prénom valide.';
        }
        if (empty($_POST['firstname'])) {
            $errorMessages['firstname'] = 'Veuillez renseigner votre prénom.';
        }
    }

    if (isset($_POST['mail'])) {
        //filtre pour éviter une regex 
        if (!filter_var($_POST['mail'], FILTER_VALIDATE_EMAIL)) {
            $errorMessages['mail'] = 'Veuillez saisir une adresse mail valide';
        }
        if (empty($_POST['mail'])) {
            $errorMessages['mail'] = 'Veuillez saisir une adresse email.';
        }
    }

    if (isset($_POST['message'])) {
        if (!preg_match($regexTextArea, $_POST['message'])) {
            $errorMessages['message'] = 'Veuillez remplir le champ correctement.';
        }
        if (empty($_POST['message'])) {
            $errorMessages['message'] = 'Veuillez remplir le champ.';
        }
    }
       
}