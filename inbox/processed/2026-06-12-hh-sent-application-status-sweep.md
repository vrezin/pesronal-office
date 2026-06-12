# HH Sent Application Status Sweep

- Date: 2026-06-12
- Source: pasted HH status selection from user

## Snapshot

User provided a selection of HH application cards with these states:

- `Просмотрен`: Ракетная фирма, Мираторг, AI Lead (585, Холдинг), Positive Technologies, Lofty, ГКУ Инфогород, AI Architect / Руководитель направления AI/Prompt-инженер, Руководитель команды агентской разработки с применением ИИ (Альфа-Банк), Руководитель направления Лид ИИ (РСХБ Факторинг)
- `Не просмотрен`: Технический лидер платформы разработки (АльфаСтрахование. ИТ), AI Solutions Architect (SKL.VC), Delivery Lead (Московская Биржа)
- `Отказ`: Инфинити, Косс Светлана Александровна, Lucky Hunter, ProBack, Холдинговая компания АлфиГрупп, AI-Native Product Technologist (НООСФЕРА)
- `Собеседование`: RapidSeedbox ltd

## Routing Outcome

- `waiting` tasks were created or kept for applications that were already sent and are now awaiting employer response.
- `done` remains the correct state for outright refusals.
- Thin cards without full JD text stay thin until the vacancy is opened and analyzed.

## Notes

- Sent applications should live in `tasks/waiting/`, even when HH shows `Просмотрен` or `Не просмотрен`.
- Rejections should live in `tasks/done/`.
- `Просмотрен` is not a reply yet; it is still a waiting state.
