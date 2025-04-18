## 🧰 Command Summary + Usage Examples

The following table summarizes all available CLI commands in `xtim` and includes usage examples for common tasks.

| Command          | Description                                                            | Example Usage                                   |
|------------------|------------------------------------------------------------------------|--------------------------------------------------|
| `xtim new`       | Create a new experiment using a Cookiecutter template                  | `xtim new`                                       |
| `xtim run`       | Run an experiment (asset or screen based)                              | `xtim run` or `xtim run --mode asset`            |
| `xtim config`    | View or edit experiment configuration (TOML, YAML)                     | `xtim config show`                               |
| `xtim devices`   | List, test, or initialize connected scientific devices                 | `xtim devices list`                              |
| `xtim assets`    | Verify, list, or test media files used in stimuli                      | `xtim assets validate`                           |
| `xtim menu`      | Launch an interactive text-based menu                                  | `xtim menu`                                      |
| `xtim export`    | Export experiment results or configuration as a ZIP or folder          | `xtim export --format zip`                       |
| `xtim archive`   | Archive a completed experiment, moving it to an archive folder         | `xtim archive my_experiment`                     |
| `xtim doctor`    | Run system diagnostics, dependency checks, and FPS/luminance tests     | `xtim doctor` or `xtim doctor --fps`             |
| `xtim info`      | Show metadata about the experiment, hardware, and environment          | `xtim info --experiment exp123`                  |
| `xtim delete`    | Remove an experiment folder or logs                                    | `xtim delete logs`                               |
| `xtim test`      | Run scientific visual timing tests (e.g., flash perception)            | `xtim test --luminance`                          |

---

### 🔄 Common Workflows

#### 🔹 1. Creating and Running a New Experiment
```bash
xtim new
cd my_experiment/
xtim run
```

#### 🔹 2. Checking Device Availability
```bash
xtim devices list
xtim devices test --device pupil
```

#### 🔹 3. Validating Stimuli Assets
```bash
xtim assets validate
```

#### 🔹 4. Exporting Results
```bash
xtim export --output results.zip
```

#### 🔹 5. Archiving Completed Experiments
```bash
xtim archive my_experiment
```

#### 🔹 6. Debugging and Diagnostics
```bash
xtim doctor status
```

#### 🔹 7. Testing
```bash
xtim test fdp
xtim test frame-rate
xtim test luminance
xtim test tic-toc
```

#### 🔹 8. Launching the Interactive Menu
```bash
xtim menu
```
---


# 🔧 Optional Flags & Parameters (examples, may vary by command)
  --mode [screen|asset]
  --experiment NAME
  --config PATH
  --simulate
  --device [pupil|emobit|millikey]
  --format [zip|folder]
  --fps
  --luminance
  --list
  --test
  --output PATH

---
# 📚 XTIM CLI – Full Command Syntax Reference

## xtim __init__
xtim __init__ [OPTIONS]

## xtim _run
xtim _run list_experiments(...)
xtim _run start(...)

## xtim archive
xtim archive archive_experiment(...)

## xtim assets
xtim assets generate_assets(...)
xtim assets shuffle_assets(...)
xtim assets import_assets(...)

## xtim config
xtim config show_config(...)
xtim config get_value(...)
xtim config set_value(...)
xtim config export_config(...)
xtim config show_experiment(...)

## xtim delete
xtim delete delete_experiment(...)

## xtim devices
xtim devices list_streams(...)

## xtim doctor
xtim doctor status(...)

## xtim export
xtim export export_experiment(...)

## xtim info
xtim info info_experiment(...)

## xtim main
xtim main [OPTIONS]

## xtim menu
xtim menu start(...)

## xtim new
xtim new experiment(...)
xtim new list_templates(...)

## xtim run
xtim run list_experiments(...)
xtim run check_environment(...)
xtim run start(...)

## xtim test
xtim test luminance(...)
xtim test frame-rate(...)
xtim test tic_toc(...)
xtim test fpd(...)

## xtim utils
xtim utils [OPTIONS]

## xtim validate
xtim validate validate_experiment(...)
