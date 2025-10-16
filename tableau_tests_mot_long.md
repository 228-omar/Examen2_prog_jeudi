# Tests unitaires pour la fonction _mot_plus_long_
- La fonction _mot_plus_long_ ne contient pas de bogues. 
- Créer au plan de tests contenant au moins 5 cas de tests **DIFFÉRENTS/VARIÉS**.
- Créer les tests unitaires pour tous les cas de tests.

| Taille de mots                          | **Résultat attendu** | **Résultat obtenue** |
|-----------------------------------------|----------------------|----------------------|
| "chat", "chien","éléphant","oiseau"     | "éléphant"           | "éléphant"           |
| "éléphant","oiseau", "souris"           | "éléphant            | "éléphant"           |
| "chat","chien","éléphant","hippopotame" | "hippopotame"        | "hippopotame"        |
| "hippopotame", 42, None, "oiseau"       | "hippopotame"        | hippopotame          |
| 42, None                                | TypeError            | TypeError            |
| "hippopotame", 42,None                  |  "hippopotame"                    | hippopotame                     |
|                                         |                      |                      |

# Tests unitaires pour la fonction _pourcentage_mots_max_
| **mots**                                     | **taille** | **Résultat attendu** | **Remarque ou Message affiché**                                      |
|----------------------------------------------|------------|----------------------|----------------------------------------------------------------------|
| ["poney", "girafe", "hippopotame", "chaton"] | 5          | 75.0                 |                                                                      |
| ["éléphant", "hippopotame", "girafe"]        | 4          | 100.0                |                                                                      |
| ["pamplemousse", 42, "cacahuète", None]      | 8          | 100.0                | "42" et None ignorés                                                 |
| []                                           | 5          | None                 | "Impossible de calculer le pourcentage. Aucun élément valide."       |
| ["chat", "chien", "rat"]                     | 5          | 0.0                  |                                                                      |
| "chat"                                       | 3          | None                 | "Impossible de calculer le pourcentage. 'chat' n'est pas une liste." |
