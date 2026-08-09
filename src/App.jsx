import { useState } from 'react'
import {
  Activity,
  Bot,
  BrainCircuit,
  CheckCircle2,
  ChevronRight,
  Clock3,
  FileText,
  LayoutDashboard,
  Menu,
  Newspaper,
  Play,
  Radio,
  RefreshCw,
  Settings,
  ShieldCheck,
  Sparkles,
  XCircle,
  Zap,
} from 'lucide-react'
import './App.css'

const posts = [
  {
    status: 'published',
    category: 'AI SECURITY',
    title: 'Why AI Agents Need Runtime Security Controls',
    description:
      'Autonomous systems introduce new attack surfaces that traditional security models may not fully address.',
    score: '94',
    time: '8 min ago',
  },
  {
    status: 'published',
    category: 'THREAT INTELLIGENCE',
    title: 'Prompt Injection Is Becoming an Agent-Level Risk',
    description:
      'New attack patterns highlight the importance of validating instructions before autonomous execution.',
    score: '91',
    time: '42 min ago',
  },
  {
    status: 'rejected',
    category: 'AI NEWS',
    title: 'The Evolution of Generative AI Models',
    description:
      'AURA determined that the topic lacked sufficient novelty and security relevance.',
    score: '42',
    time: '1 hr ago',
  },
]

const newsItems = [
  {
    source: 'ARS TECHNICA',
    title: 'New AI security research highlights risks in autonomous agents',
    time: '12 min ago',
    tag: 'SECURITY',
  },
  {
    source: 'ARS TECHNICA',
    title: 'Researchers explore new approaches to protecting AI systems',
    time: '28 min ago',
    tag: 'RESEARCH',
  },
  {
    source: 'AI SECURITY FEED',
    title: 'Prompt injection remains a major concern for AI applications',
    time: '51 min ago',
    tag: 'THREAT',
  },
  {
    source: 'TECH INTELLIGENCE',
    title: 'AI governance and runtime monitoring continue to evolve',
    time: '1 hr ago',
    tag: 'GOVERNANCE',
  },
]

function App() {
  const [analyzing, setAnalyzing] = useState(false)
  const [activePage, setActivePage] = useState('Dashboard')

  const runAnalysis = () => {
    setAnalyzing(true)

    setTimeout(() => {
      setAnalyzing(false)
    }, 2000)
  }

  const navigate = (page) => {
    setActivePage(page)
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">
            <Sparkles size={20} />
          </div>

          <div>
            <div className="brand-name">AURA</div>
            <div className="brand-subtitle">AI SECURITY</div>
          </div>
        </div>

        <nav className="nav">
          <div className="nav-section">WORKSPACE</div>

          <NavButton
            activePage={activePage}
            page="Dashboard"
            icon={<LayoutDashboard size={18} />}
            onClick={navigate}
          />

          <NavButton
            activePage={activePage}
            page="Agent"
            icon={<Bot size={18} />}
            onClick={navigate}
          />

          <NavButton
            activePage={activePage}
            page="Content"
            icon={<FileText size={18} />}
            onClick={navigate}
          />

          <NavButton
            activePage={activePage}
            page="News Feed"
            icon={<Newspaper size={18} />}
            onClick={navigate}
          />

          <div className="nav-section">SYSTEM</div>

          <NavButton
            activePage={activePage}
            page="Activity"
            icon={<Activity size={18} />}
            onClick={navigate}
          />

          <NavButton
            activePage={activePage}
            page="Settings"
            icon={<Settings size={18} />}
            onClick={navigate}
          />
        </nav>

        <div className="sidebar-bottom">
          <div className="system-status">
            <span className="status-dot" />

            <div>
              <strong>System Online</strong>
              <span>All services operational</span>
            </div>
          </div>

          <div className="version">AURA v1.0 · Autonomous AI</div>
        </div>
      </aside>

      <main className="main-content">
        <header className="topbar">
          <div className="mobile-menu">
            <Menu size={21} />
          </div>

          <div>
            <div className="breadcrumb">
              WORKSPACE / {activePage.toUpperCase()}
            </div>

            <h1>{getPageTitle(activePage)}</h1>
          </div>

          <div className="topbar-actions">
            <div className="live-indicator">
              <span />
              LIVE
            </div>

            <button className="icon-button">
              <RefreshCw size={17} />
            </button>

            <div className="avatar">A</div>
          </div>
        </header>

        {activePage === 'Dashboard' && (
          <Dashboard
            analyzing={analyzing}
            runAnalysis={runAnalysis}
            navigate={navigate}
          />
        )}

        {activePage === 'Agent' && <AgentPage runAnalysis={runAnalysis} />}

        {activePage === 'Content' && <ContentPage />}

        {activePage === 'News Feed' && <NewsFeedPage />}

        {activePage === 'Activity' && <ActivityPage />}

        {activePage === 'Settings' && <SettingsPage />}
      </main>
    </div>
  )
}

function NavButton({ activePage, page, icon, onClick }) {
  return (
    <button
      className={`nav-item ${activePage === page ? 'active' : ''}`}
      onClick={() => onClick(page)}
    >
      {icon}
      {page}
    </button>
  )
}

function getPageTitle(page) {
  const titles = {
    Dashboard: 'Autonomous Intelligence',
    Agent: 'AURA Agent',
    Content: 'Content Intelligence',
    'News Feed': 'Security News Feed',
    Activity: 'System Activity',
    Settings: 'AURA Settings',
  }

  return titles[page]
}

function Dashboard({ analyzing, runAnalysis, navigate }) {
  return (
    <>
      <section className="hero-card">
        <div className="hero-content">
          <div className="hero-label">
            <ShieldCheck size={15} />
            AUTONOMOUS AI SECURITY AGENT
          </div>

          <h2>
            Meet <span>AURA</span>
          </h2>

          <p>
            Your autonomous AI content creator that discovers, analyzes,
            evaluates and publishes relevant AI Security intelligence.
          </p>

          <div className="hero-actions">
            <button
              className="primary-button"
              onClick={runAnalysis}
              disabled={analyzing}
            >
              {analyzing ? (
                <>
                  <RefreshCw size={16} className="spin" />
                  Analyzing...
                </>
              ) : (
                <>
                  <Play size={16} />
                  Run AI Analysis
                </>
              )}
            </button>

            <button
              className="secondary-button"
              onClick={() => navigate('Activity')}
            >
              View Activity
              <ChevronRight size={16} />
            </button>
          </div>
        </div>

        <div className="hero-orbit">
          <div className="orbit orbit-one" />
          <div className="orbit orbit-two" />

          <div className="aura-core">
            <BrainCircuit size={38} />
          </div>

          <div className="orbit-node node-one">
            <Newspaper size={14} />
          </div>

          <div className="orbit-node node-two">
            <ShieldCheck size={14} />
          </div>

          <div className="orbit-node node-three">
            <Sparkles size={14} />
          </div>
        </div>
      </section>

      <section className="stats-grid">
        <StatCard
          icon={<FileText size={18} />}
          label="Published Posts"
          value="24"
          change="+12.5%"
          positive
        />

        <StatCard
          icon={<CheckCircle2 size={18} />}
          label="Approved"
          value="31"
          change="+8.2%"
          positive
        />

        <StatCard
          icon={<XCircle size={18} />}
          label="Rejected"
          value="14"
          change="Editorial filter"
        />

        <StatCard
          icon={<Zap size={18} />}
          label="Avg. AI Score"
          value="87.4"
          change="/ 100"
        />
      </section>

      <section className="dashboard-grid">
        <div className="panel content-panel">
          <div className="panel-header">
            <div>
              <div className="panel-eyebrow">CONTENT ENGINE</div>
              <h3>Recent Intelligence</h3>
            </div>

            <button
              className="text-button"
              onClick={() => navigate('Content')}
            >
              View all <ChevronRight size={15} />
            </button>
          </div>

          <div className="post-list">
            {posts.map((post) => (
              <PostCard key={post.title} {...post} />
            ))}
          </div>
        </div>

        <div className="right-column">
          <AgentCard navigate={navigate} />

          <PipelineCard />
        </div>
      </section>

      <section className="activity-bar">
        <div className="activity-left">
          <div className="activity-icon">
            <Clock3 size={16} />
          </div>

          <div>
            <strong>Last autonomous run</strong>
            <span>8 minutes ago · No new articles found</span>
          </div>
        </div>

        <div className="activity-right">
          <span>Next scheduled run</span>
          <strong>in 2 minutes</strong>
        </div>
      </section>
    </>
  )
}

function AgentPage({ runAnalysis }) {
  return (
    <div className="page-stack">
      <section className="page-intro">
        <div>
          <div className="panel-eyebrow">AUTONOMOUS AGENT</div>
          <h2>AURA #06</h2>
          <p>
            Autonomous AI Security intelligence agent configured to discover,
            analyze and generate relevant content.
          </p>
        </div>

        <span className="online-badge">
          <span />
          Online
        </span>
      </section>

      <section className="agent-page-grid">
        <div className="panel large-agent-card">
          <div className="large-agent-icon">
            <BrainCircuit size={42} />
          </div>

          <h3>AURA</h3>
          <p>AI Security Intelligence Agent</p>

          <div className="agent-page-stats">
            <div>
              <span>AGENT ID</span>
              <strong>#06</strong>
            </div>

            <div>
              <span>MODEL</span>
              <strong>Gemini AI</strong>
            </div>

            <div>
              <span>MODE</span>
              <strong>Autonomous</strong>
            </div>

            <div>
              <span>INTERVAL</span>
              <strong>10 minutes</strong>
            </div>
          </div>

          <button className="primary-button" onClick={runAnalysis}>
            <Play size={16} />
            Run Analysis
          </button>
        </div>

        <div className="panel">
          <div className="panel-eyebrow">CAPABILITIES</div>
          <h3>What AURA does</h3>

          <div className="capability-list">
            <Capability
              icon={<Newspaper size={16} />}
              title="Discover"
              text="Find relevant AI Security intelligence."
            />

            <Capability
              icon={<ShieldCheck size={16} />}
              title="Evaluate"
              text="Score relevance, novelty and security value."
            />

            <Capability
              icon={<BrainCircuit size={16} />}
              title="Reason"
              text="Make editorial decisions using AI analysis."
            />

            <Capability
              icon={<Sparkles size={16} />}
              title="Create"
              text="Generate polished security-focused content."
            />
          </div>
        </div>
      </section>
    </div>
  )
}

function ContentPage() {
  return (
    <div className="page-stack">
      <section className="page-intro">
        <div>
          <div className="panel-eyebrow">CONTENT ENGINE</div>
          <h2>Generated Intelligence</h2>
          <p>
            Review AI-generated content and editorial decisions made by AURA.
          </p>
        </div>

        <div className="content-count">24 POSTS</div>
      </section>

      <div className="content-page-list">
        {posts.map((post) => (
          <PostCard key={post.title} {...post} large />
        ))}

        <PostCard
          status="published"
          category="AI GOVERNANCE"
          title="Building Trustworthy Autonomous AI Systems"
          description="Security, governance and transparency are becoming essential components of autonomous AI deployment."
          score="89"
          time="2 hrs ago"
          large
        />
      </div>
    </div>
  )
}

function NewsFeedPage() {
  return (
    <div className="page-stack">
      <section className="page-intro">
        <div>
          <div className="panel-eyebrow">DISCOVERY ENGINE</div>
          <h2>Security News Feed</h2>
          <p>
            Recent intelligence discovered from configured security sources.
          </p>
        </div>

        <div className="live-source">
          <Radio size={14} />
          RSS ACTIVE
        </div>
      </section>

      <div className="news-grid">
        {newsItems.map((item) => (
          <article className="news-card" key={item.title}>
            <div className="news-top">
              <span>{item.source}</span>
              <span className="news-tag">{item.tag}</span>
            </div>

            <div className="news-icon">
              <Newspaper size={20} />
            </div>

            <h3>{item.title}</h3>

            <div className="news-footer">
              <span>
                <Clock3 size={13} />
                {item.time}
              </span>

              <button className="text-button">
                Analyze <ChevronRight size={14} />
              </button>
            </div>
          </article>
        ))}
      </div>
    </div>
  )
}

function ActivityPage() {
  const events = [
    ['AI Analysis', 'Topic analyzed successfully', '2 min ago', 'success'],
    ['Editorial Decision', 'Topic approved for generation', '4 min ago', 'success'],
    ['Content Generation', 'Security post generated', '5 min ago', 'success'],
    ['Duplicate Check', 'No duplicate content detected', '7 min ago', 'success'],
    ['News Discovery', 'RSS feed checked', '8 min ago', 'success'],
    ['Editorial Filter', 'Low novelty topic rejected', '1 hr ago', 'warning'],
  ]

  return (
    <div className="page-stack">
      <section className="page-intro">
        <div>
          <div className="panel-eyebrow">SYSTEM MONITOR</div>
          <h2>Activity</h2>
          <p>Recent events across the AURA autonomous workflow.</p>
        </div>
      </section>

      <div className="panel activity-list">
        {events.map(([title, text, time, type]) => (
          <div className="activity-row" key={`${title}-${time}`}>
            <div className={`activity-event-icon ${type}`}>
              {type === 'success' ? (
                <CheckCircle2 size={16} />
              ) : (
                <XCircle size={16} />
              )}
            </div>

            <div className="activity-event-content">
              <strong>{title}</strong>
              <span>{text}</span>
            </div>

            <time>{time}</time>
          </div>
        ))}
      </div>
    </div>
  )
}

function SettingsPage() {
  const [autonomousMode, setAutonomousMode] = useState(true)
  const [notifications, setNotifications] = useState(true)

  return (
    <div className="page-stack">
      <section className="page-intro">
        <div>
          <div className="panel-eyebrow">CONFIGURATION</div>
          <h2>Settings</h2>
          <p>Manage AURA's local frontend preferences.</p>
        </div>
      </section>

      <div className="settings-grid">
        <div className="panel settings-panel">
          <div className="panel-eyebrow">AGENT</div>
          <h3>Agent Configuration</h3>

          <SettingRow
            title="Autonomous Mode"
            description="Allow AURA to operate continuously."
            checked={autonomousMode}
            onChange={() => setAutonomousMode(!autonomousMode)}
          />

          <SettingRow
            title="Notifications"
            description="Show local workflow notifications."
            checked={notifications}
            onChange={() => setNotifications(!notifications)}
          />
        </div>

        <div className="panel settings-panel">
          <div className="panel-eyebrow">SYSTEM</div>
          <h3>System Information</h3>

          <InfoRow label="Version" value="AURA v1.0" />
          <InfoRow label="Agent" value="AURA #06" />
          <InfoRow label="Domain" value="AI Security" />
          <InfoRow label="Mode" value="Frontend Demo" />
        </div>
      </div>
    </div>
  )
}

function SettingRow({ title, description, checked, onChange }) {
  return (
    <div className="setting-row">
      <div>
        <strong>{title}</strong>
        <span>{description}</span>
      </div>

      <button
        className={`toggle ${checked ? 'on' : ''}`}
        onClick={onChange}
        aria-label={`Toggle ${title}`}
      >
        <span />
      </button>
    </div>
  )
}

function InfoRow({ label, value }) {
  return (
    <div className="info-row">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  )
}

function Capability({ icon, title, text }) {
  return (
    <div className="capability">
      <div className="capability-icon">{icon}</div>
      <div>
        <strong>{title}</strong>
        <span>{text}</span>
      </div>
    </div>
  )
}

function StatCard({ icon, label, value, change, positive }) {
  return (
    <div className="stat-card">
      <div className="stat-top">
        <div className="stat-icon">{icon}</div>
        {positive && <span className="stat-change">{change}</span>}
      </div>

      <div className="stat-value">{value}</div>
      <div className="stat-label">{label}</div>

      {!positive && <div className="stat-meta">{change}</div>}
    </div>
  )
}

function AgentCard({ navigate }) {
  return (
    <div className="panel agent-panel">
      <div className="panel-header">
        <div>
          <div className="panel-eyebrow">ACTIVE AGENT</div>
          <h3>AURA #06</h3>
        </div>

        <span className="online-badge">
          <span />
          Online
        </span>
      </div>

      <div className="agent-identity">
        <div className="agent-avatar">
          <BrainCircuit size={26} />
        </div>

        <div>
          <strong>AURA</strong>
          <span>AI Security Intelligence</span>
        </div>
      </div>

      <div className="agent-metrics">
        <div>
          <span>MODEL</span>
          <strong>Gemini AI</strong>
        </div>

        <div>
          <span>MODE</span>
          <strong>Autonomous</strong>
        </div>

        <div>
          <span>INTERVAL</span>
          <strong>10 min</strong>
        </div>

        <div>
          <span>SOURCE</span>
          <strong>Ars Technica</strong>
        </div>
      </div>

      <button className="agent-button" onClick={() => navigate('Agent')}>
        <Radio size={15} />
        Monitor Agent
      </button>
    </div>
  )
}

function PipelineCard() {
  return (
    <div className="panel pipeline-panel">
      <div className="panel-header">
        <div>
          <div className="panel-eyebrow">AUTOMATION</div>
          <h3>Pipeline Status</h3>
        </div>

        <Activity size={17} className="muted-icon" />
      </div>

      <PipelineItem
        icon={<Newspaper size={15} />}
        title="News Discovery"
        subtitle="RSS source"
        state="Complete"
      />

      <PipelineItem
        icon={<RefreshCw size={15} />}
        title="Duplicate Check"
        subtitle="Memory validation"
        state="Complete"
      />

      <PipelineItem
        icon={<BrainCircuit size={15} />}
        title="AI Analysis"
        subtitle="Relevance + novelty"
        state="Ready"
      />

      <PipelineItem
        icon={<Sparkles size={15} />}
        title="Content Generation"
        subtitle="Editorial pipeline"
        state="Ready"
      />
    </div>
  )
}

function PostCard({
  status,
  category,
  title,
  description,
  score,
  time,
  large = false,
}) {
  return (
    <article className={`post-card ${large ? 'post-card-large' : ''}`}>
      <div className="post-top">
        <div className="post-category">{category}</div>

        <div className={`post-status ${status}`}>
          {status === 'published' ? (
            <>
              <CheckCircle2 size={13} />
              Published
            </>
          ) : (
            <>
              <XCircle size={13} />
              Rejected
            </>
          )}
        </div>
      </div>

      <h4>{title}</h4>
      <p>{description}</p>

      <div className="post-footer">
        <span>
          <Clock3 size={13} />
          {time}
        </span>

        <span className="score">
          AI Score <strong>{score}</strong>
        </span>
      </div>
    </article>
  )
}

function PipelineItem({ icon, title, subtitle, state }) {
  return (
    <div className="pipeline-item">
      <div className="pipeline-icon">{icon}</div>

      <div className="pipeline-info">
        <strong>{title}</strong>
        <span>{subtitle}</span>
      </div>

      <div
        className={`pipeline-state ${
          state === 'Complete' ? 'complete' : ''
        }`}
      >
        {state}
      </div>
    </div>
  )
}

export default App