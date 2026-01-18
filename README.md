# AI DevOps Agent - Automated Incident Analysis & Fix PR Generator

An agentic AI system that analyzes runtime errors from application logs, identifies the root cause, generates a safe code fix, and automatically opens a GitHub Pull Request — all from a single click.

This project demonstrates how AI agents can be used beyond chat, to reason over real production signals (logs, stack traces, source code) and take concrete engineering actions.

# What this Project Does

Collects runtime error logs from a running application

Analyzes the logs to identify:

The error type

The most likely root cause

Locates the faulty method in the source code

Generates a corrected version of the code

Creates a GitHub Pull Request with the suggested fix

Stores incident history and displays it in a dashboard

All of this is triggered via a single “Run AI Agent” button in the UI.

## Why This Project Matters

Shows real agentic behavior, not just LLM prompts

Combines AI reasoning with actual engineering actions

Demonstrates fault analysis, automation, and system thinking

Highlights practical DevOps + AI integration

## High-Level Architecture

Frontend (React)
   |
   |  POST /run
   v
Backend (FastAPI)
   |
   |-- Collect logs
   |-- Run LangGraph agent workflow
   |-- Generate patch
   |-- Create GitHub PR
   |-- Store incident
   v
PostgreSQL (Incident History)


## Agent Workflow

The AI agent follows a structured flow:

Log Analysis

Reads recent runtime logs

Filters framework noise

Root Cause Identification

Explains why the error occurred in plain language

Fault Localization

Maps stack trace → source file → method

Patch Generation

Produces a minimal, safe fix

PR Creation

Pushes fix to a new branch

Opens a GitHub Pull Request automatically


## Dashboard Features

One-click Run AI Agent

Live execution logs (simulated terminal)

Root cause explanation

Generated patch diff

Direct GitHub PR link

Persistent incident history stored in PostgreSQL

## Tech Stack

Backend
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-LLM%20Agents-blueviolet)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-323330?style=flat&logo=sqlalchemy&logoColor=red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub%20API-181717?style=flat&logo=github&logoColor=white)

Frontend
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![Axios](https://img.shields.io/badge/Axios-5A29E4?style=flat)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)

Infrastructure
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Dockerized-316192?style=flat&logo=postgresql&logoColor=white)


## API Endpoints

Method	Endpoint	Description

POST	/run	    Run AI agent on latest logs
GET	    /incidents	Fetch incident history

## Example Incidents Flow

Application throws a runtime error (e.g. NullPointerException)

Logs are collected by the backend

AI agent identifies the faulty method

A corrected implementation is generated

A GitHub PR is created with the fix

Incident appears in the dashboard history


