# Job Intake Applied Status Normalization

Дата: 2026-06-10

## What Changed

- MineHub, Selby Jennings, and Shaw Daniels were normalized from `review` tasks into `waiting for reply` tasks because the applications were already submitted.
- The unknown wholesale role already had a canonical waiting task, so no duplicate active review task was kept.
- The unknown hedge fund / trading AI item remains active because the screening conversation is still open and needs a reply.

## Why

The queue should distinguish between:

- applications that are already sent and only need response tracking;
- live screening conversations that require a reply right now;
- closed outcomes that should not stay in active review.

