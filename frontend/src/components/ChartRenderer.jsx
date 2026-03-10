import {
  BarChart,
  Bar,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

function ChartRenderer({ result }) {

  if (!result || !result.data) return null;

  const data = result.data;
  const x = result.x;
  const y = result.y;
  const chart = result.chart;

  if (chart === "line") {
    return (
      <LineChart width={900} height={400} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey={x} />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey={y} stroke="#6366f1" strokeWidth={3} />
      </LineChart>
    );
  }

  return (
    <BarChart width={900} height={400} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey={x} />
      <YAxis />
      <Tooltip />
      <Bar dataKey={y} fill="#6366f1" />
    </BarChart>
  );
}

export default ChartRenderer;