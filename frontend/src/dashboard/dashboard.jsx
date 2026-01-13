//2nd version

import React, { useState, useEffect } from "react";
import { api } from "../api/api";
import {
  Bot,
  Play,
  Loader2,
  AlertTriangle,
  BrainCircuit,
  FileCode,
  GitPullRequest,
  CheckCircle2,
  Terminal,
  ChevronRight,
  Activity,
} from "lucide-react";

// Mock API response to demonstrate the UI without a backend
// const mockApiResponse = {
//   error: `ReferenceError: process is not defined
//     at /app/server/utils/logger.js:14:5
//     at Layer.handle [as handle_request] (/app/node_modules/express/lib/router/layer.js:95:5)
//     at next (/app/node_modules/express/lib/router/route.js:137:13)
//     at Route.dispatch (/app/node_modules/express/lib/router/route.js:112:3)`,
//   root_cause:
//     "The application is trying to access the Node.js global variable 'process' within a browser-side utility file that is being incorrectly imported on the client side, or the environment variables are missing in the production build context.",
//   patch: `// src/utils/logger.js
// - const env = process.env.NODE_ENV;
// + const env = typeof process !== 'undefined' ? process.env.NODE_ENV : 'development';

// export const log = (msg) => {
//   if (env === 'development') console.log(msg);
// };`,
//   pr: "https://github.com/organization/repo/pull/123",
// };

export default function DevOpsDashboard() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    if (loading) {
      setLogs([]);
      const messages = [
        "Analyzing system logs...",
        "Parsing stack traces...",
        "Querying LLM for root cause analysis...",
        "Generating fix...",
        "Creating Pull Request...",
      ];
      let i = 0;
      const interval = setInterval(() => {
        if (i < messages.length) {
          setLogs((prev) => [...prev, messages[i]]);
          i++;
        } else {
          clearInterval(interval);
        }
      }, 600);
      return () => clearInterval(interval);
    }
  }, [loading]);

  const runAgent = async () => {
    setLoading(true);
    try {
      const res = await api.post("/run");
      setResult(res.data);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full bg-slate-50 text-slate-900 pb-20 overflow-x-hidden">
      {/* Header */}
      <header className="w-full bg-white border-b border-slate-200 sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="bg-indigo-600 p-2 rounded-lg">
              <Bot className="w-5 h-5 text-white" />
            </div>
            <h1 className="font-bold text-base sm:text-md tracking-tight">
              DevOps<span className="text-indigo-600">Auto</span>Pilot
            </h1>
          </div>
          <span className="flex items-center gap-1.5 text-xs sm:text-sm text-slate-500">
            <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
            System Online
          </span>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
        {/* Hero */}
        <div className="max-w-5xl mx-auto text-center mb-10 sm:mb-12 px-2 sm:px-0">
          <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold mb-4">
            Automated Incident Response
          </h2>
          <p className="text-slate-500 max-w-lg mx-auto mb-8 text-base sm:text-lg px-2 sm:px-0">
            One-click analysis to detect errors, identify root causes, and
            automatically generate fixes for your deployment pipeline.
          </p>

          <button
            onClick={runAgent}
            disabled={loading}
            className={`w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 sm:px-8 py-3 sm:py-4 text-base sm:text-lg font-semibold rounded-full shadow-lg transition
            ${
              loading
                ? "bg-slate-800 text-white cursor-not-allowed"
                : "bg-indigo-600 text-white hover:bg-indigo-700"
            }`}
          >
            {loading ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" /> Running Agent…
              </>
            ) : (
              <>
                <Play className="w-5 h-5" /> Start Diagnosis
              </>
            )}
          </button>
        </div>

        {/* Logs */}
        {loading && (
          <div className="w-full max-w-3xl mx-auto mb-12 bg-black rounded-lg p-4 sm:p-6 text-green-400 font-mono text-xs sm:text-sm h-48 sm:h-56 overflow-y-auto">
            {logs.map((log, i) => (
              <div key={i}>❯ {log}</div>
            ))}
          </div>
        )}

        {/* Results */}
        {result && !loading && (
          <div className="grid gap-8 max-w-7xl mx-auto">
            {/* Error */}
            <div className="bg-white rounded-xl border border-red-100">
              <div className="p-4 sm:p-6 bg-red-50 flex items-center gap-2">
                <AlertTriangle className="text-red-600" />
                <h3 className="font-semibold text-red-900">Detected Error</h3>
              </div>
              <pre className="p-4 sm:p-6 text-xs sm:text-sm text-red-700 overflow-x-auto">
                {result.error}
              </pre>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* Root Cause */}
              <div className="bg-white rounded-xl border p-4 sm:p-6">
                <h3 className="font-semibold mb-2 flex items-center gap-2">
                  <BrainCircuit /> Root Cause
                </h3>
                <p className="text-slate-600">{result.root_cause}</p>
              </div>

              {/* PR */}
              <div className="bg-white rounded-xl border p-4 sm:p-6 text-center">
                <CheckCircle2 className="mx-auto text-green-600 mb-2" />
                <p className="mb-4">Fix generated and pushed.</p>
                <a
                  href={result.pr}
                  target="_blank"
                  rel="noreferrer"
                  className="text-indigo-600 hover:underline"
                >
                  View Pull Request →
                </a>
              </div>
            </div>

            {/* Patch */}
            <div className="bg-slate-900 rounded-xl text-xs sm:text-sm overflow-x-auto max-w-full">
              <div className="p-3 sm:p-4 border-b border-slate-700 flex items-center gap-2 text-slate-300">
                <FileCode /> patch.diff
              </div>
              <pre className="p-3 sm:p-6 min-w-full">
                {result.patch.split("\n").map((line, i) => (
                  <div
                    key={i}
                    className={
                      line.startsWith("+")
                        ? "text-green-400"
                        : line.startsWith("-")
                        ? "text-red-400"
                        : "text-slate-300"
                    }
                  >
                    {line}
                  </div>
                ))}
              </pre>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
