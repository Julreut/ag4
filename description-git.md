## Git-Workflow: Standardablauf für effizientes Arbeiten

Ein einfacher und robuster Git-Workflow, um häufige Probleme zu vermeiden und effizient an deinem Projekt zu arbeiten.

### Zusammenfassung

```bash
git checkout main
git pull origin main
git checkout -b feature/my-change
# Änderungen durchführen
git add .
git commit -m "Änderungen beschreiben"
git push origin feature/my-change
git checkout main
git pull origin main
git merge feature/my-change
git push origin main
git branch -d feature/my-change
git push origin --delete feature/my-change
```

### 1. Lokalen `main`-Branch aktualisieren

Bevor du mit der Arbeit beginnst, stelle sicher, dass dein lokaler `main`-Branch auf dem neuesten Stand ist:

```bash
git checkout main
git pull origin main
```

### 2. Neuen Feature-Branch erstellen

```bash
git checkout -b feature/my-change
```

### 3. Änderungen vornehmen und committen

```bash
git add .
git commit -m "Beschreibe deine Änderungen kurz und prägnant"
```

### 4. Den Feature-Branch zum Remote-Repository pushen

```bash
git push origin feature/my-change
```

Falls du zum ersten Mal pushst, setze den Upstream Branch:

```bash
git push --set-upstream origin feature/my-change
```

### 5. Änderungen im main-Branch überprüfen und mergen

```bash
git checkout main
git pull origin main
git merge feature/my-change
```

### 6. Konflikte lösen und Änderungen zum main branch pushen

```bash
git add .
git commit -m "Konflikte gelöst"
git push origin main
```
