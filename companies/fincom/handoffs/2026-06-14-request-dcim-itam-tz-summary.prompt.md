# Request Fincom Agent Summary - DCIM/ITAM ТЗ

Ты работаешь в проекте Финком (`/home/adre/projects/fincom`).

Нужно подготовить сводку по DCIM/ITAM ТЗ Ростелеком / АйТуБи с учетом текущего проектного контекста.

## Контекст

- Active entrypoint trace: `clients/pao-rostelekom/analytics/2026-06-14-dcim-itam-entrypoint-trace.md`
- Active intake log: `processes/entrypoint/intake-log.md`
- Product frame:
  - `products/packaging/catalog/product-line.md`
  - `products/packaging/catalog/technology-structure.md`
  - `products/packaging/catalog/source-materials/presentation-source-register.md`
  - `processes/ai-board/wiki/products/product-claim-register.md`
  - `products/packaging/catalog/products/`
- Important correction:
  - ITAM / asset management must be ERP/Odoo-first via `Финкомтех.ERP`, Odoo modules/extensions, and ERP Warehouse/WMS in the unified ERP database.
  - Snipe-IT / GLPI / Ralph / generic OSS asset-management systems are fallback-only after a proven ERP/Odoo gap.
- Registry constraint:
  - Treat only `Финкомтех.ERP` as currently registry-backed unless evidence says otherwise.
  - Other products/contours require registration/evidence and must not be externally promised as registered.

## Задача

Сделай короткую, но содержательную сводку по ТЗ:

1. Что заказчик, по сути, хочет получить.
2. Какие блоки ТЗ явно или вероятно закрываются существующим контуром Финкома.
3. Какие блоки частично закрываются, но требуют больших доработок.
4. Какие блоки не закрываются и требуют market/open-source candidates или отдельной разработки.
5. Какие блокеры остаются перед внешним ответом 2026-06-15.
6. Что можно безопасно сказать внешне сейчас.
7. Что нельзя говорить внешне без Evidence/Feasibility + Human Approval gates.
8. Предварительный статус: `go`, `conditional-go`, `no-go`, или `blocked`, с причиной.

## Ограничения

- Не обещай цену, срок, SLA, реестр, SCADA coverage, 3D traceability, integrations или performance без evidence.
- Не превращай презентационные claims в proof.
- Не выбирай generic OSS asset-management как primary ITAM route.
- Не делай full proposal; нужна именно presale summary для управленческого решения.

## Output

Сохрани результат в:

`clients/pao-rostelekom/analytics/2026-06-14-dcim-itam-tz-summary.md`

В конце ответа в чат напиши:

- созданный файл;
- статус;
- 5-7 ключевых выводов;
- список блокеров.
