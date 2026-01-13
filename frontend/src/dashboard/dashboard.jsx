import { useState, useEffect } from "react";
import {
  Bot,
  Play,
  Loader2,
  Terminal,
  CheckCircle2,
  AlertTriangle,
  BrainCircuit,
  ExternalLink,
  FileCode,
  History,
  RefreshCw,
} from "lucide-react";
import axios from "axios";
import { api } from "../api/api";


export default function DevOpsDashboard() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [logs, setLogs] = useState([]);

  // State for the new Incident History section
  const [incidents, setIncidents] = useState([]);
  const [isRefreshingHistory, setIsRefreshingHistory] = useState(false);

  const fetchIncidentHistory = async () => {
    try {
      const response = await api.get("/incidents");
      console.log("incident :"+ response.data);
      setIncidents(Array.isArray(response.data) ? response.data : []);
    } catch (error) {
      console.error("Error fetching incident history:", error);
    } 
  };

  useEffect(() => {
    fetchIncidentHistory();
  }, []);

  useEffect(() => {
    if (loading) {
      setLogs([]);
      const messages = [
        "Analyzing system logs...",
        "Parsing stack traces...",
        "Querying LLM for root cause analysis...",
        "Identified potential timeout constraint...",
        "Generating fix...",
        "Running regression tests...",
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
      }, 800);
      return () => clearInterval(interval);
    }
  }, [loading]);


  const runAgent = async () => {
    setLoading(true);
  
    try {
      const res = await api.post("/run");
      setResult(res.data);
      await fetchIncidentHistory();
    } finally {
      setLoading(false);
    }
  };

  const refreshHistory = async() => {
    setIsRefreshingHistory(true);
    // Simulate fetching data
    await fetchIncidentHistory();
    setIsRefreshingHistory(false);
  };

  return (
    <div className="min-h-screen w-full bg-slate-50 text-slate-900 pb-20 overflow-x-hidden font-sans">
      {/* Header */}
      <header className="w-full bg-white border-b border-slate-200 sticky top-0 z-20 shadow-sm">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="bg-indigo-600 p-2 rounded-lg shadow-md">
              <Bot className="w-5 h-5 text-white" />
            </div>
            <h2 className="font-bold tracking-tight">
              DevOps<span className="text-indigo-600">Auto</span>Pilot
            </h2>
          </div>
          <span className="flex items-center gap-2 text-xs sm:text-sm font-medium text-slate-600 bg-slate-100 px-3 py-1 rounded-full">
            <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
            System Online
          </span>
        </div>
      </header>

      <main className="max-w-5xl mx-auto px-4 sm:px-6 py-8 sm:py-12 space-y-12">
        {/* Hero Section */}
        <div className="text-center max-w-2xl mx-auto">
          <h2 className="text-3xl sm:text-4xl md:text-5xl font-extrabold mb-6 tracking-tight text-slate-900">
            Automated Incident Response
          </h2>
          <p className="text-slate-500 text-lg mb-8 leading-relaxed">
            One-click analysis to detect errors, identify root causes, and
            automatically generate fixes for your deployment pipeline.
          </p>

          <button
            onClick={runAgent}
            disabled={loading}
            className={`w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-4 text-lg font-semibold rounded-full shadow-xl hover:shadow-2xl transition-all duration-200 transform hover:-translate-y-0.5
            ${
              loading
                ? "bg-slate-800 text-slate-300 cursor-not-allowed"
                : "bg-indigo-600 text-white hover:bg-indigo-700 active:scale-95"
            }`}
          >
            {loading ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" /> Diagnosis in
                progress...
              </>
            ) : (
              <>
                <Play className="w-5 h-5 fill-current" /> Start Auto-Diagnosis
              </>
            )}
          </button>
        </div>

        {/* Live Logs Terminal */}
        {loading && (
          <div className="w-full max-w-3xl mx-auto bg-slate-950 rounded-xl overflow-hidden shadow-2xl border border-slate-800">
            <div className="bg-slate-900 px-4 py-2 flex items-center gap-2 border-b border-slate-800">
              <Terminal className="w-4 h-4 text-slate-500" />
              <span className="text-xs text-slate-400 font-mono">
                agent-logs — bash
              </span>
            </div>
            <div className="p-6 font-mono text-sm h-64 overflow-y-auto flex flex-col gap-2">
              {logs.map((log, i) => (
                <div
                  key={i}
                  className="flex gap-3 text-emerald-400 animate-in fade-in slide-in-from-left-2 duration-300"
                >
                  <span className="opacity-50 select-none">❯</span>
                  <span>{log}</span>
                </div>
              ))}
              <div className="animate-pulse text-indigo-400">_</div>
            </div>
          </div>
        )}

        {/* Diagnosis Results */}
        {result && !loading && (
          <div className="animate-in fade-in zoom-in-95 duration-500 space-y-8">
            <div className="flex items-center gap-2 text-indigo-900 bg-indigo-50 px-4 py-2 rounded-lg w-fit mx-auto border border-indigo-100">
              <CheckCircle2 className="w-5 h-5 text-indigo-600" />
              <span className="font-semibold">Analysis Complete</span>
            </div>

            <div className="grid gap-6">
              {/* Error Details */}
              <div className="bg-white rounded-xl border border-red-100 shadow-sm overflow-hidden">
                <div className="px-6 py-4 bg-red-50/50 border-b border-red-100 flex items-center gap-2">
                  <AlertTriangle className="text-red-600 w-5 h-5" />
                  <h3 className="font-semibold text-red-900">
                    Detected Exception
                  </h3>
                </div>
                <div className="p-6 bg-slate-50 overflow-x-auto">
                  <pre className="text-xs sm:text-sm text-red-700 font-mono whitespace-pre-wrap">
                    {result.error}
                  </pre>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {/* Root Cause Card */}
                <div className="bg-white rounded-xl border border-slate-200 shadow-sm p-6 flex flex-col">
                  <h3 className="font-semibold mb-4 flex items-center gap-2 text-slate-900">
                    <BrainCircuit className="text-indigo-600" /> AI Analysis
                  </h3>
                  <div className="flex-grow">
                    <p className="text-slate-600 leading-relaxed">
                      {result.root_cause}
                    </p>
                  </div>
                </div>

                {/* PR Action Card */}
                <div className="bg-white rounded-xl border border-slate-200 shadow-sm p-6 flex flex-col items-center justify-center text-center">
                  <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mb-4">
                    <CheckCircle2 className="w-6 h-6 text-green-600" />
                  </div>
                  <h3 className="font-semibold text-slate-900 mb-2">
                    Fix Generated & Pushed
                  </h3>
                  <p className="text-slate-500 text-sm mb-6">
                    A pull request has been created with the suggested patch.
                  </p>
                  <a
                    href={result.pr}
                    target="_blank"
                    rel="noreferrer"
                    className="inline-flex items-center gap-2 text-white bg-slate-900 hover:bg-slate-800 px-5 py-2.5 rounded-lg font-medium transition-colors text-sm"
                  >
                    View Pull Request <ExternalLink className="w-3 h-3" />
                  </a>
                </div>
              </div>

              {/* Patch Diff */}
              <div className="bg-slate-900 rounded-xl overflow-hidden shadow-lg border border-slate-800">
                <div className="px-4 py-3 border-b border-slate-700 flex items-center gap-2 bg-slate-950">
                  <FileCode className="w-4 h-4 text-indigo-400" />
                  <span className="text-slate-400 text-xs font-mono">
                    generated_patch.diff
                  </span>
                </div>
                <div className="p-4 overflow-x-auto">
                  <pre className="font-mono text-xs sm:text-sm">
                    {result.patch.split("\n").map((line, i) => (
                      <div
                        key={i}
                        className={`${
                          line.startsWith("+")
                            ? "bg-green-500/10 text-green-400 block w-full px-2 -mx-2 rounded"
                            : line.startsWith("-")
                            ? "bg-red-500/10 text-red-400 block w-full px-2 -mx-2 rounded"
                            : "text-slate-400 pl-2"
                        }`}
                      >
                        {line}
                      </div>
                    ))}
                  </pre>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* -------------------------------------------------------------
            NEW SECTION: INCIDENT HISTORY
            Adapted from the user's snippet into the Tailwind design
           ------------------------------------------------------------- */}
        <div className="pt-12 mt-12 border-t border-slate-200">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-slate-900 flex items-center gap-2">
              <History className="text-slate-400" /> Incident History
            </h2>
            <button
              onClick={refreshHistory}
              disabled={isRefreshingHistory}
              className="text-sm flex items-center gap-2 text-indigo-600 hover:text-indigo-700 font-medium px-4 py-2 hover:bg-indigo-50 rounded-lg transition-colors"
            >
              <RefreshCw
                className={`w-4 h-4 ${
                  isRefreshingHistory ? "animate-spin" : ""
                }`}
              />
              {isRefreshingHistory ? "Refreshing..." : "Refresh History"}
            </button>
          </div>

          <div className="space-y-4">
            {incidents.length === 0 ? (
              <div className="text-center py-12 bg-white rounded-xl border border-dashed border-slate-300 text-slate-500">
                No incidents recorded.
              </div>
            ) : (
              Array.isArray(incidents) && incidents.map((incident) => (
                <div
                  key={incident.id}
                  className="bg-white rounded-xl border border-slate-200 p-5 shadow-sm hover:shadow-md transition-shadow group"
                >
                  <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-4 mb-3">
                    <div className="flex items-start gap-3">
                      <div className="mt-1 min-w-[20px]">
                        <div className="w-2 h-2 mt-1.5 rounded-full bg-red-500"></div>
                      </div>
                      <div>
                        <h4 className="font-semibold text-slate-900 text-sm sm:text-base mb-1 line-clamp-1">
                          {incident.error.split(":")[0]}
                        </h4>
                        <p className="text-xs text-slate-400 font-mono mb-2">
                          {new Date(incident.createds_at).toLocaleString()}
                        </p>
                      </div>
                    </div>

                    <a
                      href={incident.pr}
                      target="_blank"
                      rel="noreferrer"
                      className="shrink-0 inline-flex items-center gap-1.5 text-xs font-medium text-indigo-600 bg-indigo-50 hover:bg-indigo-100 px-3 py-1.5 rounded-md transition-colors w-fit"
                    >
                      View PR <ExternalLink className="w-3 h-3" />
                    </a>
                  </div>

                  <div className="pl-8 text-sm space-y-2">
                    <div className="p-3 bg-red-50 rounded-lg border border-red-100">
                      <span className="font-semibold text-red-900 text-xs uppercase tracking-wider block mb-1">
                        Error Log
                      </span>
                      <code className="text-red-800 break-words block text-xs sm:text-sm">
                        {incident.error}
                      </code>
                    </div>

                    <div className="flex items-start gap-2 text-slate-600 mt-2">
                      <BrainCircuit className="w-4 h-4 text-indigo-500 mt-0.5 shrink-0" />
                      <span className="text-sm">
                        <span className="font-medium text-slate-700">
                          Root Cause:
                        </span>{" "}
                        {incident.root_cause}
                      </span>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </main>
    </div>
  );
}